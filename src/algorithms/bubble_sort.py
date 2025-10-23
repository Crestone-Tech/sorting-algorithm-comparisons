"""Bubble Sort algorithm implementation with instrumentation"""

from typing import List, Any, Optional
from src.algorithms.base import SortingAlgorithm
from src.instrumentation.metrics import PerformanceMetrics


class BubbleSort(SortingAlgorithm):
    """
    Bubble Sort algorithm implementation.
    
    Time Complexity:
        - Best: O(n) when array is already sorted
        - Average: O(n²)
        - Worst: O(n²)
    
    Space Complexity: O(1) - sorts in place
    
    Stable: Yes - maintains relative order of equal elements
    """
    
    def __init__(self):
        self.metrics: Optional[PerformanceMetrics] = None
    
    @property
    def name(self) -> str:
        return "Bubble Sort"
    
    @property
    def description(self) -> str:
        return (
            "A simple comparison-based sorting algorithm that repeatedly steps "
            "through the list, compares adjacent elements, and swaps them if "
            "they are in the wrong order."
        )
    
    def sort(self, data: List[Any]) -> List[Any]:
        """
        Sort the given data using bubble sort algorithm.
        
        Args:
            data: List of comparable items to sort
            
        Returns:
            Sorted list (sorted in place, but also returned)
        """
        # Initialize metrics
        self.metrics = PerformanceMetrics(
            algorithm_name=self.name,
            input_size=len(data)
        )
        self.metrics.start_timer()
        
        # Make a copy to avoid modifying the original
        arr = data.copy()
        n = len(arr)
        
        # Bubble sort algorithm with instrumentation
        for i in range(n):
            # Flag to optimize: if no swaps occur, array is sorted
            swapped = False
            
            for j in range(0, n - i - 1):
                # Increment array access counter (accessing arr[j] and arr[j+1])
                self.metrics.increment_array_accesses(2)
                
                # Compare adjacent elements
                self.metrics.increment_comparisons()
                if arr[j] > arr[j + 1]:
                    # Swap if they're in wrong order
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.metrics.increment_swaps()
                    self.metrics.increment_array_accesses(2)  # For the swap
                    swapped = True
            
            # If no swaps occurred, array is sorted
            if not swapped:
                self.metrics.metadata["early_termination"] = True
                self.metrics.metadata["iterations_saved"] = n - i - 1
                break
        
        # Stop timer and calculate memory
        self.metrics.stop_timer()
        self.metrics.memory_used_bytes = arr.__sizeof__()
        
        return arr
    
    def get_metrics(self) -> Optional[PerformanceMetrics]:
        """
        Get the performance metrics from the last sort operation.
        
        Returns:
            PerformanceMetrics object or None if sort hasn't been called
        """
        return self.metrics

