"""Base class for sorting algorithms"""

from abc import ABC, abstractmethod
from typing import List, Any


class SortingAlgorithm(ABC):
    """Abstract base class for all sorting algorithms"""
    
    @abstractmethod
    def sort(self, data: List[Any]) -> List[Any]:
        """
        Sort the given data and return the sorted result.
        
        Args:
            data: List of comparable items to sort
            
        Returns:
            Sorted list
        """
        pass
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Return the name of the sorting algorithm"""
        pass
    
    @property
    @abstractmethod
    def description(self) -> str:
        """Return a description of the sorting algorithm"""
        pass

