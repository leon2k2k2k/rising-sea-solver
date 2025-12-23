"""
Improved FOAG PDF Parser with better text extraction and cleaning
"""

import pdfplumber
import re
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple
from enum import Enum

class ContentType(Enum):
    EXERCISE = "exercise"
    DEFINITION = "definition"
    THEOREM = "theorem"
    EXAMPLE = "example"
    REMARK = "remark"

@dataclass
class CleanMathContent:
    """Cleaned version of mathematical content"""
    content_type: ContentType
    number: str
    raw_text: str
    cleaned_text: str
    parts: List[str]  # For multi-part exercises
    page_number: int
    chapter: int

class ImprovedFOAGParser:
    """Better FOAG parser with improved text extraction"""
    
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        
    def extract_clean_text_from_pages(self, start_page: int, end_page: int) -> str:
        """Extract and clean text from a page range"""
        all_text = ""
        
        with pdfplumber.open(self.pdf_path) as pdf:
            for page_num in range(start_page - 1, min(end_page, len(pdf.pages))):
                page = pdf.pages[page_num]
                
                # Extract text with better settings
                text = page.extract_text(
                    x_tolerance=3,
                    y_tolerance=3,
                    layout=True,
                    x_density=7.25,
                    y_density=13
                )
                
                if text:
                    # Clean up the text
                    text = self._clean_page_text(text)
                    all_text += f"\\n--- PAGE {page_num + 1} ---\\n{text}\\n"
        
        return all_text
    
    def _clean_page_text(self, text: str) -> str:
        """Clean up text from a single page"""
        if not text:
            return ""
        
        # Fix common OCR issues
        text = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', text)  # Add space before capitals
        text = re.sub(r'(?<=[.!?])(?=[A-Z])', ' ', text)  # Space after sentence endings
        text = re.sub(r'\\s+', ' ', text)  # Multiple spaces to single
        text = re.sub(r'\\n\\s*\\n\\s*', '\\n\\n', text)  # Clean up multiple newlines
        
        # Fix common mathematical notation issues
        text = text.replace('→', ' → ')
        text = text.replace('↗', ' ↗ ')
        text = text.replace('⇒', ' ⇒ ')
        text = text.replace('∼', ' ∼ ')
        text = text.replace('↔', ' ↔ ')
        
        return text.strip()
    
    def find_exercises_manual(self, text: str) -> List[CleanMathContent]:
        """Manually identify and extract exercises with better parsing"""
        exercises = []
        
        # Split into pages
        pages = text.split('--- PAGE')
        
        for page_section in pages:
            if not page_section.strip():
                continue
                
            # Extract page number
            page_match = re.search(r'(\\d+) ---', page_section)
            page_num = int(page_match.group(1)) if page_match else 0
            
            # The actual FOAG pattern is "1.1. A. EXERCISE." with spaces
            # Look for exercise patterns - using the correct format we observed
            exercise_patterns = [
                # Pattern: "1.1. A. UNIMPORTANT EXERCISE." or "1.1. B. EXERCISE."
                r'(\\d+\\.\\d+\\. [A-Z]\\.)\\s*((?:UNIMPORTANT\\s+)?EXERCISE)\\s*\\.\\s*([^\\n]*(?:\\n(?!\\d+\\.\\d+\\. [A-Z]\\. (?:UNIMPORTANT\\s+)?EXERCISE)[^\\n]*)*)',
                
                # Alternative pattern for other exercise formats
                r'(\\d+\\.\\d+\\.[A-Z]\\.)\\s*((?:UNIMPORTANT\\s+)?EXERCISE)\\s*\\.\\s*([^\\n]*(?:\\n(?!\\d+\\.\\d+\\.[A-Z]\\. (?:UNIMPORTANT\\s+)?EXERCISE)[^\\n]*)*)'
            ]
            
            for pattern in exercise_patterns:
                matches = re.finditer(pattern, page_section, re.MULTILINE | re.DOTALL)
                
                for match in matches:
                    number_part = match.group(1).replace(' ', '').replace('.', '.') # Convert "1.1. A." to "1.1.A"
                    number = number_part.rstrip('.')
                    exercise_type = match.group(2)
                    content = match.group(3).strip()
                    
                    # Skip if content is too short or seems wrong
                    if len(content) < 20:
                        continue
                    
                    # Clean the content more aggressively
                    content = self._clean_exercise_content(content)
                    
                    # Split multi-part exercises
                    parts = self._split_multipart_exercise(content)
                    
                    exercise = CleanMathContent(
                        content_type=ContentType.EXERCISE,
                        number=number,
                        raw_text=match.group(0),
                        cleaned_text=content,
                        parts=parts,
                        page_number=page_num,
                        chapter=1
                    )
                    
                    exercises.append(exercise)
                    print(f"Found exercise {number} on page {page_num}")
        
        return exercises
    
    def _clean_exercise_content(self, content: str) -> str:
        """Clean exercise content more thoroughly"""
        
        # Remove obvious parsing artifacts
        content = re.sub(r'©\\d{4}.*?Press\\.\\s*\\d+', '', content)  # Copyright notice
        content = re.sub(r'Pre-publication.*?Geometry', '', content)  # Header
        
        # Fix word boundaries
        content = re.sub(r'([a-z])([A-Z])', r'\\1 \\2', content)
        
        # Fix common concatenations
        fixes = {
            'isomorphismis': 'isomorphism is',
            'Aisanobject': 'A is an object',
            'showthat': 'show that',
            'ifandonlyif': 'if and only if',
            'suchthat': 'such that',
            'forall': 'for all',
            'thereexists': 'there exists',
            'Thatis': 'That is',
            'Inother': 'In other',
            'Wehavean': 'We have an',
            'Supposewe': 'Suppose we',
            'Letusdefine': 'Let us define',
            'Notethat': 'Note that'
        }
        
        for bad, good in fixes.items():
            content = content.replace(bad, good)
        
        # Clean up whitespace again
        content = re.sub(r'\\s+', ' ', content)
        content = re.sub(r'\\n\\s*\\n\\s*', '\\n\\n', content)
        
        return content.strip()
    
    def _split_multipart_exercise(self, content: str) -> List[str]:
        """Split multi-part exercises (a), (b), etc."""
        parts = []
        
        # Look for (a), (b), (c) pattern
        part_pattern = r'\\([a-z]\\)\\s*([^\\n]*(?:\\n(?!\\([a-z]\\))[^\\n]*)*)'
        matches = list(re.finditer(part_pattern, content, re.MULTILINE | re.DOTALL))
        
        if matches:
            for match in matches:
                part_letter = match.group(0)[1]  # Extract letter
                part_content = match.group(1).strip()
                parts.append(f"({part_letter}) {part_content}")
        else:
            # No multi-part structure found
            parts = [content]
        
        return parts
    
    def extract_chapter_1_exercises(self) -> List[CleanMathContent]:
        """Extract Chapter 1 exercises with improved parsing"""
        
        print("Extracting text from FOAG Chapter 1...")
        
        # Chapter 1 is roughly pages 29-70 based on our previous analysis
        raw_text = self.extract_clean_text_from_pages(29, 70)
        
        print("Finding exercises in extracted text...")
        exercises = self.find_exercises_manual(raw_text)
        
        print(f"Found {len(exercises)} exercises")
        
        # Debug: save raw text for inspection
        with open('debug_raw_text.txt', 'w', encoding='utf-8') as f:
            f.write(raw_text)
        
        return exercises
    
    def export_clean_exercises(self, exercises: List[CleanMathContent], filename: str):
        """Export cleaned exercises"""
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("# FOAG Chapter 1 Exercises (Cleaned)\\n\\n")
            
            for exercise in exercises:
                f.write(f"## Exercise {exercise.number}\\n\\n")
                f.write(f"**Page:** {exercise.page_number}\\n\\n")
                
                if len(exercise.parts) > 1:
                    f.write("**Multi-part exercise:**\\n\\n")
                    for part in exercise.parts:
                        f.write(f"{part}\\n\\n")
                else:
                    f.write(f"**Content:**\\n{exercise.cleaned_text}\\n\\n")
                
                f.write("---\\n\\n")

if __name__ == "__main__":
    parser = ImprovedFOAGParser("FOAG.pdf")
    exercises = parser.extract_chapter_1_exercises()
    
    parser.export_clean_exercises(exercises, "cleaned_chapter1_exercises.md")
    print(f"Exported {len(exercises)} cleaned exercises")
    
    # Show first few for verification
    for i, ex in enumerate(exercises[:3]):
        print(f"\\n=== EXERCISE {ex.number} ===")
        print(f"Page: {ex.page_number}")
        print(f"Content preview: {ex.cleaned_text[:200]}...")
        if len(ex.parts) > 1:
            print(f"Parts: {len(ex.parts)}")