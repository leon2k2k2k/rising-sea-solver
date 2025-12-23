"""
Exercise parsing module for FOAG textbook.

Implements both deterministic (regex-based) and agent-based approaches
for extracting exercises from LaTeX mathematical texts.
"""

import re
import json
import sys
import os
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass
from pathlib import Path

# Add project root to path for imports
sys.path.append(str(Path(__file__).parent.parent.parent))
from together import Together


@dataclass
class Exercise:
    """Represents a single exercise from the textbook."""
    id: str
    title: str
    content: str
    start_line: Optional[int] = None
    end_line: Optional[int] = None
    extraction_method: str = "unknown"
    confidence: float = 1.0


class DeterministicExerciseExtractor:
    """Extracts exercises using deterministic regex patterns."""
    
    def __init__(self):
        self.exercise_patterns = [
            # Pattern 1: \subsubsection*{1.1.A. Unimportant Exercise}
            (r'\\subsubsection\*\{([^}]*(?:[Ee]xercise|EXERCISE)[^}]*)\}(.*?)(?=\\subsubsection|\Z)', 
             "subsubsection_exercise"),
            
            # Pattern 2: \begin{exercise}...\end{exercise}
            (r'\\begin\{exercise\}(.*?)\\end\{exercise\}', 
             "environment_exercise"),
            
            # Pattern 3: \subsubsection*{1.1.C. EXERCISE.}
            (r'\\subsubsection\*\{(\d+\.\d+\.[A-Z]\.\s*EXERCISE[^}]*)\}(.*?)(?=\\subsubsection|\Z)', 
             "numbered_exercise"),
            
            # Pattern 4: Any section with "Exercise" in title
            (r'\\subsubsection\*\{([^}]*[Ee]xercise[^}]*)\}(.*?)(?=\\subsubsection|\\section|\\subsection|\Z)', 
             "general_exercise")
        ]
    
    def extract_exercises(self, latex_content: str) -> List[Exercise]:
        """Extract exercises using deterministic patterns."""
        exercises = []
        lines = latex_content.split('\n')
        
        for pattern, pattern_name in self.exercise_patterns:
            matches = re.finditer(pattern, latex_content, re.DOTALL | re.IGNORECASE)
            
            for match in matches:
                # Extract exercise ID from title
                title = match.group(1) if len(match.groups()) > 1 else match.group(1)
                content = match.group(2) if len(match.groups()) > 1 else match.group(1)
                
                # Clean up content
                content = content.strip()
                title = title.strip()
                
                # Extract exercise ID (like "1.1.A")
                exercise_id = self._extract_exercise_id(title)
                
                # Find line numbers
                start_pos = match.start()
                end_pos = match.end()
                start_line = latex_content[:start_pos].count('\n') + 1
                end_line = latex_content[:end_pos].count('\n') + 1
                
                exercise = Exercise(
                    id=exercise_id,
                    title=title,
                    content=content,
                    start_line=start_line,
                    end_line=end_line,
                    extraction_method=f"deterministic_{pattern_name}",
                    confidence=1.0
                )
                
                exercises.append(exercise)
        
        # Remove duplicates (same exercise matched by multiple patterns)
        exercises = self._deduplicate_exercises(exercises)
        
        return exercises
    
    def _extract_exercise_id(self, title: str) -> str:
        """Extract exercise ID from title."""
        # Look for patterns like "1.1.A", "1.1.B", "1.1.C", etc.
        id_match = re.search(r'(\d+\.\d+\.[A-Z])', title)
        if id_match:
            return id_match.group(1)
        
        # Fallback: look for any number-letter combination
        fallback_match = re.search(r'(\d+\.\d+\.[A-Za-z]+)', title)
        if fallback_match:
            return fallback_match.group(1)
        
        # Last resort: generate from title
        return title.replace(' ', '_').replace('.', '').lower()[:20]
    
    def _deduplicate_exercises(self, exercises: List[Exercise]) -> List[Exercise]:
        """Remove duplicate exercises based on content similarity."""
        if not exercises:
            return exercises
        
        unique_exercises = []
        seen_content = set()
        
        for exercise in exercises:
            # Use first 100 characters of content as fingerprint
            content_fingerprint = exercise.content[:100].strip()
            
            if content_fingerprint not in seen_content:
                unique_exercises.append(exercise)
                seen_content.add(content_fingerprint)
        
        return unique_exercises


class AgentBasedExerciseExtractor:
    """Extracts exercises using LLM agent."""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or "tgp_v1_0ljNvqYPTMCc1_VLyNCCUj2Jg3v3P8-lmgOBRYMHJ1c"
        self.client = Together(api_key=self.api_key)
        self.model = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"
    
    def extract_exercises(self, latex_content: str) -> List[Exercise]:
        """Extract exercises using LLM agent."""
        prompt = self._create_extraction_prompt()
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": f"Extract all exercises from this LaTeX content:\n\n{latex_content}"}
                ],
                temperature=0.1,  # Low temperature for consistency
                max_tokens=4000
            )
            
            result_text = response.choices[0].message.content
            exercises = self._parse_agent_response(result_text, latex_content)
            
            return exercises
            
        except Exception as e:
            print(f"Agent extraction failed: {e}")
            return []
    
    def _create_extraction_prompt(self) -> str:
        """Create extraction prompt for the LLM."""
        return """You are a mathematical text parser specializing in LaTeX documents. Your task is to extract ALL exercises from the given LaTeX content.

Look for exercises in these formats:
1. \\subsubsection*{1.1.A. Unimportant Exercise} followed by exercise content
2. \\subsubsection*{1.1.B. Exercise} followed by exercise content  
3. \\subsubsection*{1.1.C. EXERCISE.} followed by exercise content
4. \\begin{exercise}...\\end{exercise} environments
5. Any section that contains exercise problems

For each exercise found, extract:
- Exercise ID (like "1.1.A", "1.1.B", etc.)
- Title/description
- Full exercise content (including sub-parts like (a), (b), etc.)
- Approximate line numbers if possible

Return your results in this EXACT JSON format:
```json
{
    "exercises": [
        {
            "id": "1.1.A", 
            "title": "Unimportant Exercise",
            "content": "A category in which each morphism is an isomorphism is called a groupoid...",
            "confidence": 0.95
        }
    ]
}
```

Be thorough and capture ALL exercises. Include the complete exercise text, not summaries."""
    
    def _parse_agent_response(self, response_text: str, original_content: str) -> List[Exercise]:
        """Parse the agent's JSON response into Exercise objects."""
        exercises = []
        
        try:
            # Extract JSON from response (handle cases where agent adds extra text)
            json_match = re.search(r'```json\s*(.*?)\s*```', response_text, re.DOTALL)
            if json_match:
                json_text = json_match.group(1)
            else:
                # Try to find JSON without markdown formatting
                json_text = response_text
            
            # Fix common JSON escape issues in LaTeX content
            json_text = json_text.replace('\\\\', '\\\\\\\\')  # Fix LaTeX double backslashes
            json_text = json_text.replace('\\"', '\\\\"')      # Fix escaped quotes
            json_text = json_text.replace('\\{', '\\\\{')      # Fix LaTeX braces
            json_text = json_text.replace('\\}', '\\\\}')      # Fix LaTeX braces
            
            # Parse JSON
            data = json.loads(json_text)
            
            for ex_data in data.get("exercises", []):
                # Find line numbers by searching for content in original
                start_line, end_line = self._find_line_numbers(
                    ex_data.get("content", ""), original_content
                )
                
                exercise = Exercise(
                    id=ex_data.get("id", "unknown"),
                    title=ex_data.get("title", ""),
                    content=ex_data.get("content", ""),
                    start_line=start_line,
                    end_line=end_line,
                    extraction_method="agent_based",
                    confidence=ex_data.get("confidence", 0.8)
                )
                exercises.append(exercise)
                
        except json.JSONDecodeError as e:
            print(f"Failed to parse agent response as JSON: {e}")
            # Try to extract exercises using fallback regex parsing
            exercises = self._fallback_parse_agent_response(response_text)
            
        except Exception as e:
            print(f"Error parsing agent response: {e}")
        
        return exercises
    
    def _fallback_parse_agent_response(self, response_text: str) -> List[Exercise]:
        """Fallback parsing when JSON fails."""
        exercises = []
        
        # Look for exercise patterns in the response text
        exercise_patterns = [
            r'"id":\s*"([^"]+)".*?"title":\s*"([^"]+)".*?"content":\s*"([^"]+(?:[^"\\]|\\.)*)"',
            r'Exercise\s+(\d+\.\d+\.[A-Z])[:\s]+([^\n]+)'
        ]
        
        for pattern in exercise_patterns:
            matches = re.finditer(pattern, response_text, re.DOTALL | re.IGNORECASE)
            for match in matches:
                if len(match.groups()) >= 3:
                    exercise = Exercise(
                        id=match.group(1),
                        title=match.group(2),
                        content=match.group(3),
                        extraction_method="agent_based_fallback",
                        confidence=0.6
                    )
                    exercises.append(exercise)
        
        return exercises
    
    def _find_line_numbers(self, content: str, original_content: str) -> Tuple[Optional[int], Optional[int]]:
        """Find approximate line numbers for content in original text."""
        if not content or not original_content:
            return None, None
        
        # Look for a distinctive part of the content
        content_words = content.split()[:10]  # First 10 words
        search_phrase = " ".join(content_words)
        
        lines = original_content.split('\n')
        for i, line in enumerate(lines):
            if search_phrase.lower() in line.lower():
                # Found start, now estimate end
                content_lines = content.count('\n') + 5  # Add buffer
                return i + 1, min(i + content_lines + 1, len(lines))
        
        return None, None


class HybridExerciseExtractor:
    """Combines deterministic and agent-based approaches."""
    
    def __init__(self, api_key: str = None):
        self.deterministic = DeterministicExerciseExtractor()
        self.agent = AgentBasedExerciseExtractor(api_key)
    
    def extract_exercises(self, latex_content: str, use_agent: bool = True) -> List[Exercise]:
        """Extract exercises using hybrid approach."""
        # Step 1: Deterministic extraction
        deterministic_exercises = self.deterministic.extract_exercises(latex_content)
        
        if not use_agent:
            return deterministic_exercises
        
        # Step 2: Agent-based extraction
        agent_exercises = self.agent.extract_exercises(latex_content)
        
        # Step 3: Merge and deduplicate
        all_exercises = deterministic_exercises + agent_exercises
        merged_exercises = self._merge_exercises(all_exercises)
        
        return merged_exercises
    
    def _merge_exercises(self, exercises: List[Exercise]) -> List[Exercise]:
        """Merge exercise lists, preferring higher confidence extractions."""
        if not exercises:
            return []
        
        # Group by exercise ID
        exercises_by_id = {}
        for exercise in exercises:
            if exercise.id not in exercises_by_id:
                exercises_by_id[exercise.id] = []
            exercises_by_id[exercise.id].append(exercise)
        
        # For each ID, pick the best extraction
        merged = []
        for exercise_id, candidates in exercises_by_id.items():
            # Sort by confidence, then by method preference
            candidates.sort(key=lambda x: (x.confidence, x.extraction_method == "deterministic"), reverse=True)
            merged.append(candidates[0])
        
        # Sort by exercise ID for consistent output
        merged.sort(key=lambda x: x.id)
        
        return merged


def main():
    """Test the exercise extraction on FOAG files."""
    # Test file path
    test_file = Path(__file__).parent.parent.parent / "data" / "latex" / "FOAG_1_1_copy.tex"
    
    if not test_file.exists():
        print(f"Test file not found: {test_file}")
        return
    
    # Read the LaTeX content
    with open(test_file, 'r', encoding='utf-8') as f:
        latex_content = f.read()
    
    print("=== Testing Exercise Extraction ===\n")
    
    # Test deterministic extraction
    print("1. Deterministic Extraction:")
    deterministic_extractor = DeterministicExerciseExtractor()
    det_exercises = deterministic_extractor.extract_exercises(latex_content)
    
    for ex in det_exercises:
        print(f"  - {ex.id}: {ex.title}")
        print(f"    Method: {ex.extraction_method}")
        print(f"    Lines: {ex.start_line}-{ex.end_line}")
        print(f"    Content preview: {ex.content[:100]}...")
        print()
    
    # Test agent extraction
    print("\n2. Agent-based Extraction:")
    agent_extractor = AgentBasedExerciseExtractor()
    agent_exercises = agent_extractor.extract_exercises(latex_content)
    
    for ex in agent_exercises:
        print(f"  - {ex.id}: {ex.title}")
        print(f"    Method: {ex.extraction_method}")
        print(f"    Confidence: {ex.confidence}")
        print(f"    Content preview: {ex.content[:100]}...")
        print()
    
    # Test hybrid extraction
    print("\n3. Hybrid Extraction:")
    hybrid_extractor = HybridExerciseExtractor()
    hybrid_exercises = hybrid_extractor.extract_exercises(latex_content)
    
    for ex in hybrid_exercises:
        print(f"  - {ex.id}: {ex.title}")
        print(f"    Method: {ex.extraction_method}")
        print(f"    Confidence: {ex.confidence}")
        print()
    
    print(f"\nSummary:")
    print(f"  Deterministic found: {len(det_exercises)} exercises")
    print(f"  Agent found: {len(agent_exercises)} exercises") 
    print(f"  Hybrid result: {len(hybrid_exercises)} exercises")


if __name__ == "__main__":
    main()