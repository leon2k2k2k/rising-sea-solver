"""
Core Exercise class and related data structures.
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Dict, Optional, Any
from pathlib import Path
import json


class ExerciseStatus(Enum):
    """Status of exercise solving process."""
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress" 
    COMPLETED = "completed"


class SolutionStatus(Enum):
    """Status of a solution attempt."""
    ATTEMPT = "attempt"
    APPROVED = "approved"
    REJECTED = "rejected"


@dataclass
class Solution:
    """Represents a solution to an exercise."""
    content: str
    status: SolutionStatus = SolutionStatus.ATTEMPT
    model_name: str = ""  # Model that generated this solution
    proof_comment: List[str] = field(default_factory=list)  # Comments on the proof
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass 
class Exercise:
    """
    Exercise representation for parsing and solution tracking.
    """
    
    # Basic identification
    id: str  # Like "1.1.A", "1.1.B"
    title: str
    content: str
    
    # Source information
    source_file: Optional[Path] = None
    start_line: Optional[int] = None
    end_line: Optional[int] = None
    chapter: Optional[str] = None
    section: Optional[str] = None
    
    # Solution tracking
    status: ExerciseStatus = ExerciseStatus.NOT_STARTED
    solutions: List[Solution] = field(default_factory=list)
    
    # Extraction metadata
    extraction_method: str = "unknown"
    extraction_confidence: float = 1.0
    extraction_timestamp: datetime = field(default_factory=datetime.now)
    
    def add_solution(self, solution: Solution) -> None:
        """Add a new solution attempt."""
        self.solutions.append(solution)
        
        # Update status based on solution status
        if solution.status == SolutionStatus.APPROVED:
            self.status = ExerciseStatus.COMPLETED
        elif solution.status == SolutionStatus.ATTEMPT:
            if self.status == ExerciseStatus.NOT_STARTED:
                self.status = ExerciseStatus.IN_PROGRESS
    
    def get_approved_solution(self) -> Optional[Solution]:
        """Get the approved solution if one exists."""
        for solution in self.solutions:
            if solution.status == SolutionStatus.APPROVED:
                return solution
        return None
    
    def mark_completed(self) -> None:
        """Mark exercise as completed."""
        self.status = ExerciseStatus.COMPLETED
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'status': self.status.value,
            'solutions': [
                {
                    'content': s.content,
                    'status': s.status.value,
                    'model_name': s.model_name,
                    'proof_comment': s.proof_comment,
                    'timestamp': s.timestamp.isoformat()
                } for s in self.solutions
            ],
            'source_file': str(self.source_file) if self.source_file else None,
            'start_line': self.start_line,
            'end_line': self.end_line,
            'chapter': self.chapter,
            'section': self.section,
            'extraction_method': self.extraction_method,
            'extraction_timestamp': self.extraction_timestamp.isoformat()}
    
    def to_json(self, file_path: Optional[Path] = None) -> str:
        """Export to JSON format."""
        data = self.to_dict()
        json_str = json.dumps(data, indent=2, ensure_ascii=False)
        
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(json_str)
        
        return json_str
    
    def __str__(self) -> str:
        return f"Exercise {self.id}: {self.title} ({self.status.value})"
    
    def __repr__(self) -> str:
        return f"Exercise(id='{self.id}', title='{self.title}', status={self.status})"