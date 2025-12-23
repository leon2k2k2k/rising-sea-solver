"""
Debug script to examine the actual text content from FOAG Chapter 1
"""

import pdfplumber

def debug_chapter_1():
    with pdfplumber.open("FOAG.pdf") as pdf:
        # Let's look at more pages to find actual Chapter 1 content
        for page_num in range(20, 40):  # Look at pages 21-40
            if page_num < len(pdf.pages):
                page = pdf.pages[page_num]
                text = page.extract_text()
                
                # Look for actual chapter 1 start
                if "1.1" in text and "categor" in text.lower():
                    print(f"\n=== POTENTIAL CHAPTER 1 START: PAGE {page_num + 1} ===")
                    print(text[:1500])  # First 1500 characters
                    print("...")
                    
                    # Look for exercise patterns in this page
                    if "exercise" in text.lower():
                        print(f"\n*** Found 'exercise' on page {page_num + 1} ***")
                        # Show context around exercises
                        lines = text.split('\n')
                        for i, line in enumerate(lines):
                            if 'exercise' in line.lower():
                                start = max(0, i-2)
                                end = min(len(lines), i+3)
                                print("EXERCISE CONTEXT:")
                                for j in range(start, end):
                                    print(f"  {lines[j]}")
                                print()

if __name__ == "__main__":
    debug_chapter_1()