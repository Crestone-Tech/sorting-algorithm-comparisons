"""Performance metrics collection for sorting algorithms"""

from dataclasses import dataclass, field
from typing import Optional
import time


@dataclass
class PerformanceMetrics:
    """Container for performance metrics collected during sorting"""
    
    # Time metrics
    execution_time_ms: float = 0.0
    start_time: Optional[float] = None
    end_time: Optional[float] = None
    
    # Operation counts
    comparisons: int = 0
    swaps: int = 0
    array_accesses: int = 0
    
    # Memory metrics
    memory_used_bytes: int = 0
    
    # Algorithm info
    algorithm_name: str = ""
    input_size: int = 0
    
    # Additional metadata
    metadata: dict = field(default_factory=dict)
    
    def start_timer(self) -> None:
        """Start the execution timer"""
        self.start_time = time.perf_counter()
    
    def stop_timer(self) -> None:
        """Stop the execution timer and calculate elapsed time"""
        if self.start_time is None:
            raise ValueError("Timer was not started")
        self.end_time = time.perf_counter()
        self.execution_time_ms = (self.end_time - self.start_time) * 1000
    
    def increment_comparisons(self, count: int = 1) -> None:
        """Increment comparison counter"""
        self.comparisons += count
    
    def increment_swaps(self, count: int = 1) -> None:
        """Increment swap counter"""
        self.swaps += count
    
    def increment_array_accesses(self, count: int = 1) -> None:
        """Increment array access counter"""
        self.array_accesses += count
    
    def to_dict(self) -> dict:
        """Convert metrics to dictionary"""
        return {
            "algorithm_name": self.algorithm_name,
            "input_size": self.input_size,
            "execution_time_ms": round(self.execution_time_ms, 4),
            "comparisons": self.comparisons,
            "swaps": self.swaps,
            "array_accesses": self.array_accesses,
            "memory_used_bytes": self.memory_used_bytes,
            "metadata": self.metadata
        }

