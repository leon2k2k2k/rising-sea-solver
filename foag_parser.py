"""
FOAG PDF Parser - Extract and structure content from Vakil's FOAG textbook
Focus on Chapter 1: Basic category theory and presheaves
"""

import pdfplumber
import re
from dataclasses import dataclass
from typing import List, Dict, Optional, Tuple
from enum import Enum

class ContentType(Enum):
    DEFINITION = "definition"
    THEOREM = "theorem" 
    LEMMA = "lemma"
    PROPOSITION = "proposition"
    COROLLARY = "corollary"
    EXERCISE = "exercise"
    EXAMPLE = "example"
    REMARK = "remark"
    PROOF = "proof"
    TEXT = "text"

@dataclass
class MathContent:
    """Represents a piece of mathematical content from FOAG"""
    content_type: ContentType
    number: Optional[str]  # e.g., "1.2.3" for exercises, theorems
    title: Optional[str]
    content: str
    latex_math: List[str]  # Extracted mathematical expressions
    references: List[str]  # Referenced theorems, definitions, etc.
    chapter: int
    page_number: int
    
class FOAGParser:
    """Parser for FOAG PDF focusing on Chapter 1"""
    
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.chapter_1_content = []
        
    def extract_chapter_1(self) -> List[MathContent]:
        """Extract and parse Chapter 1 content"""
        
        with pdfplumber.open(self.pdf_path) as pdf:
            chapter_1_pages = self._find_chapter_1_pages(pdf)
            
            for page_num in chapter_1_pages:
                page = pdf.pages[page_num]
                raw_text = page.extract_text()
                
                # Process the text to identify mathematical structures
                content_items = self._parse_page_content(raw_text, page_num + 1)
                self.chapter_1_content.extend(content_items)
                
        return self.chapter_1_content
    
    def _find_chapter_1_pages(self, pdf) -> List[int]:
        """Find the page range for Chapter 1"""
        chapter_1_start = None
        chapter_2_start = None
        
        for page_num, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                # Look for actual Chapter 1 content (around page 29)
                if page_num >= 25 and ("1.1" in text and "categor" in text.lower()):
                    if chapter_1_start is None:
                        chapter_1_start = page_num
                        print(f"Found Chapter 1 start at page {page_num + 1}")
                elif ("Chapter 2" in text or "2.1" in text) and "sheav" in text.lower() and chapter_1_start is not None:
                    chapter_2_start = page_num
                    print(f"Found Chapter 2 start at page {page_num + 1}")
                    break
                    
        if chapter_1_start is None:
            # Fallback: use pages around where we expect Chapter 1 content
            print("Could not find Chapter 1 markers, using pages 29-70 as estimate")
            return list(range(28, 70))  # Pages 29-70 (0-indexed)
            
        return list(range(chapter_1_start, chapter_2_start or min(chapter_1_start + 50, len(pdf.pages))))
    
    def _parse_page_content(self, text: str, page_num: int) -> List[MathContent]:
        """Parse a single page to extract mathematical content"""
        content_items = []
        
        # Regular expressions for different content types in FOAG format
        patterns = {
            # FOAG exercises have format like "1.1.A. EXERCISE." or "1.2.B. EXERCISE."
            ContentType.EXERCISE: r'(\d+\.\d+\.[A-Z]+)\.\s*(?:UNIMPORTANT\s+)?EXERCISE\.\s*(.*?)(?=\n\s*\d+\.\d+\.[A-Z]+\.\s*(?:UNIMPORTANT\s+)?EXERCISE\.|$)',
            
            # Definitions often have format "1.2.1. Definition."
            ContentType.DEFINITION: r'(\d+\.\d+\.\d+)\.\s*Definition\.\s*(.*?)(?=\n\s*\d+\.\d+\.\d+\.|$)',
            
            # Theorems, lemmas, etc.
            ContentType.THEOREM: r'(\d+\.\d+\.\d+)\.\s*(?:Theorem|Important\s+Example)\.\s*(.*?)(?=\n\s*\d+\.\d+\.\d+\.|$)',
            ContentType.LEMMA: r'(\d+\.\d+\.\d+)\.\s*Lemma\.\s*(.*?)(?=\n\s*\d+\.\d+\.\d+\.|$)',
            
            # Examples often have format "1.1.2. Example."
            ContentType.EXAMPLE: r'(\d+\.\d+\.\d+)\.\s*(?:Example|Important\s+Example)\.\s*(.*?)(?=\n\s*\d+\.\d+\.\d+\.|$)',
        }
        
        # Clean up the text - FOAG sometimes has formatting issues
        text = re.sub(r'\n+', '\n', text)  # Multiple newlines to single
        text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)  # Fix missing spaces
        
        for content_type, pattern in patterns.items():
            matches = re.finditer(pattern, text, re.DOTALL | re.IGNORECASE)
            
            for match in matches:
                number = match.group(1)
                content = match.group(2).strip()
                
                # Clean up the content
                content = re.sub(r'\s+', ' ', content)  # Multiple spaces to single
                content = content.strip()
                
                # Skip if content is too short (likely parsing error)
                if len(content) < 10:
                    continue
                
                # Extract LaTeX math expressions
                latex_math = self._extract_latex_math(content)
                
                # Extract references to other theorems, definitions, etc.
                references = self._extract_references(content)
                
                math_content = MathContent(
                    content_type=content_type,
                    number=number,
                    title=None,
                    content=content,
                    latex_math=latex_math,
                    references=references,
                    chapter=1,
                    page_number=page_num
                )
                
                content_items.append(math_content)
        
        return content_items
    
    def _extract_latex_math(self, text: str) -> List[str]:
        """Extract LaTeX mathematical expressions from text"""
        # Match both inline math $...$ and display math $$...$$
        inline_math = re.findall(r'\$(.*?)\$', text)
        display_math = re.findall(r'\$\$(.*?)\$\$', text, re.DOTALL)
        
        return inline_math + display_math
    
    def _extract_references(self, text: str) -> List[str]:
        """Extract references to theorems, definitions, exercises, etc."""
        # Look for patterns like "Theorem 1.2.3", "Definition 1.4", etc.
        ref_pattern = r'(Theorem|Definition|Lemma|Proposition|Exercise|Example)\s+(\d+(?:\.\d+)*)'
        references = re.findall(ref_pattern, text, re.IGNORECASE)
        
        return [f"{ref_type} {number}" for ref_type, number in references]
    
    def get_exercises_only(self) -> List[MathContent]:
        """Get only the exercises from Chapter 1"""
        return [item for item in self.chapter_1_content 
                if item.content_type == ContentType.EXERCISE]
    
    def export_for_llm(self, output_path: str):
        """Export parsed content in a format suitable for LLM processing"""
        exercises = self.get_exercises_only()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# FOAG Chapter 1 Exercises\n\n")
            f.write("Extracted from Vakil's Foundations of Algebraic Geometry\n\n")
            
            for exercise in exercises:
                f.write(f"## Exercise {exercise.number}\n\n")
                f.write(f"**Page**: {exercise.page_number}\n\n")
                f.write(f"**Content**:\n{exercise.content}\n\n")
                
                if exercise.latex_math:
                    f.write("**Mathematical Expressions**:\n")
                    for math_expr in exercise.latex_math:
                        f.write(f"- `{math_expr}`\n")
                    f.write("\n")
                
                if exercise.references:
                    f.write("**References**:\n")
                    for ref in exercise.references:
                        f.write(f"- {ref}\n")
                    f.write("\n")
                
                f.write("---\n\n")

if __name__ == "__main__":
    # Example usage
    parser = FOAGParser("FOAG.pdf")
    
    try:
        content = parser.extract_chapter_1()
        print(f"Extracted {len(content)} content items from Chapter 1")
        
        exercises = parser.get_exercises_only()
        print(f"Found {len(exercises)} exercises")
        
        # Export for LLM processing
        parser.export_for_llm("chapter1_exercises.md")
        print("Exported exercises to chapter1_exercises.md")
        
    except Exception as e:
        print(f"Error parsing PDF: {e}")
        import traceback
        traceback.print_exc()