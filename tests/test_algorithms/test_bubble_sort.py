"""Tests for Bubble Sort algorithm"""

import pytest
from src.algorithms.bubble_sort import BubbleSort


class TestBubbleSort:
    """Test suite for Bubble Sort implementation"""
    
    def test_sort_unsorted_array(self, sample_data, sorted_data):
        """Test sorting an unsorted array"""
        sorter = BubbleSort()
        result = sorter.sort(sample_data)
        assert result == sorted_data
    
    def test_sort_already_sorted(self, sorted_data):
        """Test sorting an already sorted array"""
        sorter = BubbleSort()
        result = sorter.sort(sorted_data)
        assert result == sorted_data
    
    def test_sort_reverse_sorted(self, reverse_sorted_data, sorted_data):
        """Test sorting a reverse sorted array"""
        sorter = BubbleSort()
        result = sorter.sort(reverse_sorted_data)
        assert result == sorted_data
    
    def test_sort_empty_array(self):
        """Test sorting an empty array"""
        sorter = BubbleSort()
        result = sorter.sort([])
        assert result == []
    
    def test_sort_single_element(self):
        """Test sorting a single element array"""
        sorter = BubbleSort()
        result = sorter.sort([42])
        assert result == [42]
    
    def test_sort_duplicates(self):
        """Test sorting an array with duplicate values"""
        sorter = BubbleSort()
        data = [5, 2, 8, 2, 9, 1, 5]
        expected = [1, 2, 2, 5, 5, 8, 9]
        result = sorter.sort(data)
        assert result == expected
    
    def test_sort_negative_numbers(self):
        """Test sorting an array with negative numbers"""
        sorter = BubbleSort()
        data = [3, -1, 4, -5, 2, -3]
        expected = [-5, -3, -1, 2, 3, 4]
        result = sorter.sort(data)
        assert result == expected
    
    def test_sort_floats(self):
        """Test sorting an array of floats"""
        sorter = BubbleSort()
        data = [3.14, 2.71, 1.41, 1.73]
        expected = [1.41, 1.73, 2.71, 3.14]
        result = sorter.sort(data)
        assert result == expected
    
    def test_sort_strings(self):
        """Test sorting an array of strings"""
        sorter = BubbleSort()
        data = ["banana", "apple", "cherry", "date"]
        expected = ["apple", "banana", "cherry", "date"]
        result = sorter.sort(data)
        assert result == expected
    
    def test_original_array_unchanged(self, sample_data):
        """Test that original array is not modified"""
        sorter = BubbleSort()
        original = sample_data.copy()
        sorter.sort(sample_data)
        assert sample_data == original
    
    def test_metrics_collected(self, sample_data):
        """Test that performance metrics are collected"""
        sorter = BubbleSort()
        sorter.sort(sample_data)
        metrics = sorter.get_metrics()
        
        assert metrics is not None
        assert metrics.algorithm_name == "Bubble Sort"
        assert metrics.input_size == len(sample_data)
        assert metrics.execution_time_ms > 0
        assert metrics.comparisons > 0
        assert metrics.array_accesses > 0
    
    def test_metrics_comparisons_count(self):
        """Test that comparisons are counted correctly"""
        sorter = BubbleSort()
        data = [3, 2, 1]
        sorter.sort(data)
        metrics = sorter.get_metrics()
        
        # For [3,2,1]: worst case for 3 elements
        # Should have some comparisons
        assert metrics.comparisons > 0
    
    def test_metrics_swaps_count(self):
        """Test that swaps are counted correctly"""
        sorter = BubbleSort()
        data = [3, 2, 1]
        sorter.sort(data)
        metrics = sorter.get_metrics()
        
        # Reverse sorted array should require swaps
        assert metrics.swaps > 0
    
    def test_early_termination_optimization(self, sorted_data):
        """Test that early termination occurs for sorted arrays"""
        sorter = BubbleSort()
        sorter.sort(sorted_data)
        metrics = sorter.get_metrics()
        
        # Should terminate early
        assert metrics.metadata.get("early_termination") == True
    
    def test_name_property(self):
        """Test the name property"""
        sorter = BubbleSort()
        assert sorter.name == "Bubble Sort"
    
    def test_description_property(self):
        """Test the description property"""
        sorter = BubbleSort()
        assert len(sorter.description) > 0
        assert "comparison" in sorter.description.lower()

