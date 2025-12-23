"""
Comprehensive Memory-Based FOAG Chapter 1 Parser

This parser extracts and structures all content from FOAG Chapter 1 into memory
for efficient access during problem solving. It identifies and categorizes:
- Definitions, theorems, lemmas, propositions, corollaries
- Exercises (including multi-part)
- Examples and remarks
- Mathematical expressions and references

The content is stored in memory with efficient lookup capabilities.
"""

import pdfplumber
import re
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Union, Set
from enum import Enum
import json

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
    SECTION = "section"
    TEXT = "text"

@dataclass
class MathContent:
    """Represents a piece of mathematical content"""
    content_type: ContentType
    number: str  # e.g., "1.1.A", "1.2.3", "Definition 1.1.1"
    title: Optional[str]
    content: str
    clean_content: str  # Cleaned version for processing
    page_numbers: List[int]
    parts: List[str] = field(default_factory=list)  # For multi-part content
    references: Set[str] = field(default_factory=set)  # Referenced items
    keywords: Set[str] = field(default_factory=set)  # Key mathematical terms
    
    def __post_init__(self):
        """Extract keywords and references after initialization"""
        self.keywords = self._extract_keywords()
        self.references = self._extract_references()
    
    def _extract_keywords(self) -> Set[str]:
        """Extract mathematical keywords from content"""
        # Common mathematical terms to identify
        math_patterns = [
            r'\b(?:category|categories|functor|morphism|isomorphism|object|natural transformation)\b',
            r'\b(?:group|ring|field|module|vector space|algebra)\b',
            r'\b(?:commutative|associative|identity|inverse|bijective|injective|surjective)\b',
            r'\b(?:kernel|cokernel|quotient|product|coproduct|limit|colimit)\b'
        ]
        
        keywords = set()
        text = self.clean_content.lower()
        for pattern in math_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            keywords.update(matches)
        
        return keywords
    
    def _extract_references(self) -> Set[str]:
        """Extract references to other numbered items"""
        patterns = [
            r'Definition\s+(\d+\.\d+\.\d+)',
            r'Theorem\s+(\d+\.\d+\.\d+)',
            r'Exercise\s+(\d+\.\d+\.[A-Z])',
            r'Example\s+(\d+\.\d+\.\d+)',
            r'Lemma\s+(\d+\.\d+\.\d+)'
        ]
        
        refs = set()
        for pattern in patterns:
            matches = re.findall(pattern, self.content, re.IGNORECASE)
            refs.update(matches)
        
        return refs

class FOAGMemoryParser:
    """Memory-based parser for FOAG Chapter 1"""
    
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.content_database: Dict[str, MathContent] = {}
        self.content_by_type: Dict[ContentType, List[MathContent]] = {
            ct: [] for ct in ContentType
        }
        self.keyword_index: Dict[str, Set[str]] = {}  # keyword -> content numbers
        
    def parse_chapter(self) -> Dict[str, MathContent]:
        """Parse entire Chapter 1 and store in memory"""
        print("Starting comprehensive parse of FOAG Chapter 1...")
        
        with pdfplumber.open(self.pdf_path) as pdf:
            # Chapter 1 typically starts around page 29 and goes to about page 70
            chapter_text = self._extract_chapter_text(pdf, start_page=29, end_page=70)
            
            # Parse different content types
            self._parse_exercises(chapter_text)
            self._parse_definitions(chapter_text) 
            self._parse_theorems_and_lemmas(chapter_text)
            self._parse_examples_and_remarks(chapter_text)
            
            # Build indexes for efficient lookup
            self._build_indexes()
            
        print(f"Parsed {len(self.content_database)} items from Chapter 1")
        return self.content_database
    
    def _extract_chapter_text(self, pdf, start_page: int, end_page: int) -> str:
        """Extract clean text from chapter pages"""
        all_text = ""
        
        for page_num in range(start_page - 1, min(end_page, len(pdf.pages))):
            page = pdf.pages[page_num]
            
            # Use optimized extraction settings
            text = page.extract_text(
                x_tolerance=2,
                y_tolerance=2,
                layout=True,
                x_density=7.25,
                y_density=13
            )
            
            if text:
                # Clean the text
                cleaned_text = self._clean_page_text(text, page_num + 1)
                all_text += f"\n--- PAGE {page_num + 1} ---\n{cleaned_text}\n"
        
        return all_text
    
    def _clean_page_text(self, text: str, page_num: int) -> str:
        """Clean extracted text from a single page"""
        if not text:
            return ""
        
        # Remove header/footer patterns
        lines = text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            
            # Skip headers, footers, page numbers
            if (re.match(r'^\d+\s*$', line) or  # page numbers
                re.match(r'^©.*Vakil.*Princeton.*', line) or  # copyright
                len(line) < 3 or  # very short lines
                re.match(r'^\s*\d+\s*$', line)):  # standalone numbers
                continue
            
            cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines)
    
    def _parse_exercises(self, text: str):
        """Parse all exercises from the text"""
        # Pattern for exercises: EXERCISE 1.1.A, etc.
        exercise_pattern = r'EXERCISE\s+(\d+\.\d+\.[A-Z])'
        
        matches = list(re.finditer(exercise_pattern, text, re.IGNORECASE))
        
        for i, match in enumerate(matches):
            number = match.group(1)
            start_pos = match.start()
            
            # Find end position (next exercise or major section)
            if i + 1 < len(matches):
                end_pos = matches[i + 1].start()
            else:
                # Look for next major section or end of text
                next_section = re.search(r'\n\s*\d+\.\d+\.\s+[A-Z]', text[start_pos + 100:])
                if next_section:
                    end_pos = start_pos + 100 + next_section.start()
                else:
                    end_pos = len(text)
            
            # Extract content
            content = text[start_pos:end_pos].strip()
            
            # Clean and split into parts if needed
            clean_content = self._clean_exercise_content(content)
            parts = self._split_exercise_parts(clean_content)
            
            # Extract page numbers
            page_numbers = self._extract_page_numbers(content)
            
            # Create content object
            exercise = MathContent(
                content_type=ContentType.EXERCISE,
                number=number,
                title=f"Exercise {number}",
                content=content,
                clean_content=clean_content,
                page_numbers=page_numbers,
                parts=parts
            )
            
            self.content_database[number] = exercise
            self.content_by_type[ContentType.EXERCISE].append(exercise)
    
    def _parse_definitions(self, text: str):
        """Parse definitions from the text"""
        # Look for numbered definitions
        def_pattern = r'(\d+\.\d+\.\d+)\.\s*Definition[^.]*?\.'
        
        for match in re.finditer(def_pattern, text, re.IGNORECASE):
            number = match.group(1)
            
            # Extract surrounding context for full definition
            start_pos = max(0, match.start() - 50)
            end_pos = min(len(text), match.end() + 500)
            content = text[start_pos:end_pos]
            
            # Clean content
            clean_content = re.sub(r'\s+', ' ', content).strip()
            
            # Extract page numbers
            page_numbers = self._extract_page_numbers(content)
            
            definition = MathContent(
                content_type=ContentType.DEFINITION,
                number=f"Definition {number}",
                title=f"Definition {number}",
                content=content,
                clean_content=clean_content,
                page_numbers=page_numbers
            )
            
            self.content_database[f"def_{number}"] = definition
            self.content_by_type[ContentType.DEFINITION].append(definition)
    
    def _parse_theorems_and_lemmas(self, text: str):
        """Parse theorems, lemmas, propositions, corollaries"""
        patterns = {
            ContentType.THEOREM: r'(\d+\.\d+\.\d+)\.\s*Theorem[^.]*?\.',
            ContentType.LEMMA: r'(\d+\.\d+\.\d+)\.\s*Lemma[^.]*?\.',
            ContentType.PROPOSITION: r'(\d+\.\d+\.\d+)\.\s*Proposition[^.]*?\.',
            ContentType.COROLLARY: r'(\d+\.\d+\.\d+)\.\s*Corollary[^.]*?\.'
        }
        
        for content_type, pattern in patterns.items():
            for match in re.finditer(pattern, text, re.IGNORECASE):
                number = match.group(1)
                
                # Extract context
                start_pos = max(0, match.start() - 50)
                end_pos = min(len(text), match.end() + 800)
                content = text[start_pos:end_pos]
                
                clean_content = re.sub(r'\s+', ' ', content).strip()
                page_numbers = self._extract_page_numbers(content)
                
                item = MathContent(
                    content_type=content_type,
                    number=f"{content_type.value.title()} {number}",
                    title=f"{content_type.value.title()} {number}",
                    content=content,
                    clean_content=clean_content,
                    page_numbers=page_numbers
                )
                
                key = f"{content_type.value}_{number}"
                self.content_database[key] = item
                self.content_by_type[content_type].append(item)
    
    def _parse_examples_and_remarks(self, text: str):
        """Parse examples and remarks"""
        patterns = {
            ContentType.EXAMPLE: r'(\d+\.\d+\.\d+)\.\s*Example[^.]*?\.',
            ContentType.REMARK: r'(\d+\.\d+\.\d+)\.\s*Remark[^.]*?\.'
        }
        
        for content_type, pattern in patterns.items():
            for match in re.finditer(pattern, text, re.IGNORECASE):
                number = match.group(1)
                
                start_pos = max(0, match.start() - 30)
                end_pos = min(len(text), match.end() + 600)
                content = text[start_pos:end_pos]
                
                clean_content = re.sub(r'\s+', ' ', content).strip()
                page_numbers = self._extract_page_numbers(content)
                
                item = MathContent(
                    content_type=content_type,
                    number=f"{content_type.value.title()} {number}",
                    title=f"{content_type.value.title()} {number}",
                    content=content,
                    clean_content=clean_content,
                    page_numbers=page_numbers
                )
                
                key = f"{content_type.value}_{number}"
                self.content_database[key] = item
                self.content_by_type[content_type].append(item)
    
    def _clean_exercise_content(self, content: str) -> str:
        """Clean exercise content for better processing"""
        # Remove extra whitespace and normalize
        cleaned = re.sub(r'\s+', ' ', content).strip()
        
        # Remove page markers
        cleaned = re.sub(r'--- PAGE \d+ ---', '', cleaned)
        
        return cleaned
    
    def _split_exercise_parts(self, content: str) -> List[str]:
        """Split multi-part exercises into parts"""
        # Look for (a), (b), (c) etc.
        part_pattern = r'\([a-z]\)'
        
        if not re.search(part_pattern, content):
            return [content]
        
        parts = []
        splits = re.split(part_pattern, content)
        
        # First split is the main question
        if splits[0].strip():
            parts.append(splits[0].strip())
        
        # Add lettered parts
        for i, part in enumerate(splits[1:], ord('a')):
            if part.strip():
                parts.append(f"({chr(i)}) {part.strip()}")
        
        return parts
    
    def _extract_page_numbers(self, content: str) -> List[int]:
        """Extract page numbers from content"""
        page_matches = re.findall(r'--- PAGE (\d+) ---', content)
        return [int(p) for p in page_matches]
    
    def _build_indexes(self):
        """Build keyword and reference indexes for fast lookup"""
        for content in self.content_database.values():
            # Build keyword index
            for keyword in content.keywords:
                if keyword not in self.keyword_index:
                    self.keyword_index[keyword] = set()
                self.keyword_index[keyword].add(content.number)
    
    # Access methods for the in-memory database
    
    def get_exercises(self) -> List[MathContent]:
        """Get all exercises"""
        return self.content_by_type[ContentType.EXERCISE]
    
    def get_definitions(self) -> List[MathContent]:
        """Get all definitions"""
        return self.content_by_type[ContentType.DEFINITION]
    
    def get_by_number(self, number: str) -> Optional[MathContent]:
        """Get content by number (e.g., '1.1.A', 'def_1.1.1')"""
        return self.content_database.get(number)
    
    def search_by_keyword(self, keyword: str) -> List[MathContent]:
        """Search content containing a keyword"""
        results = []
        keyword_lower = keyword.lower()
        
        for content in self.content_database.values():
            if (keyword_lower in content.clean_content.lower() or
                keyword_lower in content.keywords):
                results.append(content)
        
        return results
    
    def get_content_summary(self) -> Dict[str, int]:
        """Get summary of parsed content"""
        return {
            content_type.value: len(items) 
            for content_type, items in self.content_by_type.items()
            if items
        }
    
    def save_to_json(self, filepath: str):
        """Save parsed content to JSON file"""
        # Convert to serializable format
        serializable = {}
        for key, content in self.content_database.items():
            serializable[key] = {
                'content_type': content.content_type.value,
                'number': content.number,
                'title': content.title,
                'content': content.content,
                'clean_content': content.clean_content,
                'page_numbers': content.page_numbers,
                'parts': content.parts,
                'references': list(content.references),
                'keywords': list(content.keywords)
            }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(serializable, f, indent=2, ensure_ascii=False)

# Convenience function to create and run parser
def parse_foag_chapter_1(pdf_path: str = "FOAG-chp-1.pdf") -> FOAGMemoryParser:
    """Parse FOAG Chapter 1 and return the memory parser with loaded content"""
    parser = FOAGMemoryParser(pdf_path)
    parser.parse_chapter()
    return parser

if __name__ == "__main__":
    # Example usage
    parser = parse_foag_chapter_1()
    
    print("=== PARSING COMPLETE ===")
    print(f"Content summary: {parser.get_content_summary()}")
    
    # Show some exercises
    exercises = parser.get_exercises()
    print(f"\nFound {len(exercises)} exercises:")
    for ex in exercises[:3]:  # Show first 3
        print(f"- {ex.number}: {ex.content[:100]}...")
    
    # Save to JSON for persistence
    parser.save_to_json("foag_chapter1_parsed.json")
    print("\nSaved parsed content to foag_chapter1_parsed.json")