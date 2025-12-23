"""
Simple direct parser for FOAG exercises
"""

import pdfplumber
import re
from typing import List, Dict

def extract_foag_exercises_simple():
    """Extract exercises directly using simple text search"""
    
    exercises = []
    
    with pdfplumber.open("FOAG.pdf") as pdf:
        # Check pages 29-70 for exercises
        for page_num in range(28, 70):  # 0-indexed
            if page_num >= len(pdf.pages):
                break
                
            page = pdf.pages[page_num]
            text = page.extract_text()
            
            if not text:
                continue
            
            # Look for lines that contain "EXERCISE"
            lines = text.split('\\n')
            
            for i, line in enumerate(lines):
                if 'EXERCISE' in line and any(char.isdigit() for char in line):
                    
                    # Found an exercise line - extract the exercise number and content
                    print(f"\\nFound exercise on page {page_num + 1}:")
                    print(f"Line: {line}")
                    
                    # Extract a few lines after for content
                    content_lines = []
                    for j in range(i, min(i + 10, len(lines))):
                        content_lines.append(lines[j])
                        # Stop if we hit another exercise or section
                        if j > i and ('EXERCISE' in lines[j] or lines[j].strip().startswith('1.') and 'Definition' in lines[j]):
                            break
                    
                    content = '\\n'.join(content_lines)
                    
                    # Try to extract exercise number
                    number_match = re.search(r'(\\d+\\.\\d+\\.\\s*[A-Z])', line)
                    if number_match:
                        number = number_match.group(1).replace(' ', '')
                    else:
                        number = f"Page{page_num + 1}"
                    
                    exercise = {
                        'number': number,
                        'page': page_num + 1,
                        'raw_line': line,
                        'content': content,
                        'content_preview': content[:200] + '...' if len(content) > 200 else content
                    }
                    
                    exercises.append(exercise)
                    print(f"Exercise {number}: {content[:100]}...")
    
    return exercises

if __name__ == "__main__":
    print("Searching for FOAG exercises...")
    exercises = extract_foag_exercises_simple()
    
    print(f"\\n\\n=== SUMMARY ===")
    print(f"Found {len(exercises)} exercises")
    
    # Save results
    with open('simple_exercise_extraction.txt', 'w') as f:
        f.write("FOAG Exercise Extraction Results\\n\\n")
        
        for ex in exercises:
            f.write(f"Exercise: {ex['number']} (Page {ex['page']})\\n")
            f.write(f"Raw line: {ex['raw_line']}\\n")
            f.write(f"Content preview: {ex['content_preview']}\\n")
            f.write("---\\n\\n")
    
    print("Results saved to simple_exercise_extraction.txt")