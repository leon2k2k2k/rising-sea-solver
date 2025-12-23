#!/usr/bin/env python3
"""
Test script for exercise parsing and JSON storage.
"""

import sys
from pathlib import Path
import json

# Add src to path
sys.path.append(str(Path(__file__).parent))

from src.parsing.parsing_exercises import HybridExerciseExtractor


def test_parsing_and_save():
    """Test parsing exercises and save them as JSON files."""
    
    # Path to FOAG LaTeX file
    latex_file = Path("data/latex/FOAG_1_1_copy.tex")
    exercises_dir = Path("data/exercises")
    
    print("=== FOAG Exercise Extraction and JSON Storage ===\n")
    
    # Check if LaTeX file exists
    if not latex_file.exists():
        print(f"Error: LaTeX file not found at {latex_file}")
        return
    
    # Read LaTeX content
    print(f"Reading LaTeX file: {latex_file}")
    with open(latex_file, 'r', encoding='utf-8') as f:
        latex_content = f.read()
    
    print(f"File size: {len(latex_content)} characters")
    print(f"Lines: {latex_content.count('n') + 1}")
    
    # Extract exercises using hybrid approach
    print("\nExtracting exercises using hybrid approach...")
    extractor = HybridExerciseExtractor()
    exercises = extractor.extract_exercises(latex_content)
    
    print(f"Found {len(exercises)} exercises")
    
    if not exercises:
        print("No exercises found. Check the LaTeX content and parsing patterns.")
        return
    
    # Display extracted exercises
    print("\n=== Extracted Exercises ===")
    for i, exercise in enumerate(exercises, 1):
        print(f"\n{i}. Exercise {exercise.id}")
        print(f"   Title: {exercise.title}")
        print(f"   Method: {exercise.extraction_method}")
        print(f"   Confidence: {exercise.extraction_confidence}")
        print(f"   Lines: {exercise.start_line}-{exercise.end_line}")
        print(f"   Content preview: {exercise.content[:150]}...")
    
    # Save exercises as JSON files
    print(f"\n=== Saving to JSON ===")
    exercises_dir.mkdir(exist_ok=True)
    
    # Save all exercises in one file
    all_exercises_file = exercises_dir / "foag_1_1_exercises.json"
    exercises_data = [ex.to_dict() for ex in exercises]
    
    with open(all_exercises_file, 'w', encoding='utf-8') as f:
        json.dump(exercises_data, f, indent=2, ensure_ascii=False)
    
    print(f"Saved all exercises to: {all_exercises_file}")
    
    # Save individual exercise files
    individual_dir = exercises_dir / "individual"
    individual_dir.mkdir(exist_ok=True)
    
    for exercise in exercises:
        filename = f"exercise_{exercise.id.replace('.', '_')}.json"
        individual_file = individual_dir / filename
        
        with open(individual_file, 'w', encoding='utf-8') as f:
            json.dump(exercise.to_dict(), f, indent=2, ensure_ascii=False)
        
        print(f"Saved {exercise.id} to: {individual_file}")
    
    # Save summary
    summary = {
        "source_file": str(latex_file),
        "extraction_date": str(Path().absolute()),
        "total_exercises": len(exercises),
        "exercises": [
            {
                "id": ex.id,
                "title": ex.title,
                "method": ex.extraction_method,
                "confidence": ex.extraction_confidence
            } for ex in exercises
        ]
    }
    
    summary_file = exercises_dir / "extraction_summary.json"
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    
    print(f"Saved extraction summary to: {summary_file}")
    
    print(f"\n=== Storage Summary ===")
    print(f"- All exercises: {all_exercises_file}")
    print(f"- Individual files: {individual_dir}")
    print(f"- Summary: {summary_file}")
    print(f"- Total exercises extracted: {len(exercises)}")


if __name__ == "__main__":
    test_parsing_and_save()