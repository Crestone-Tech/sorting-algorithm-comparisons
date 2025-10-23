"""Pytest configuration and shared fixtures"""

import pytest


@pytest.fixture
def sample_data():
    """Provide sample data for testing sorting algorithms"""
    return [64, 34, 25, 12, 22, 11, 90]


@pytest.fixture
def sorted_data():
    """Provide already sorted data for testing"""
    return [11, 12, 22, 25, 34, 64, 90]


@pytest.fixture
def reverse_sorted_data():
    """Provide reverse sorted data for testing"""
    return [90, 64, 34, 25, 22, 12, 11]

@pytest.fixture
def data_with_duplicates_unsorted():
    """Provide unsorted data with duplicates for testing"""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

@pytest.fixture
def data_with_duplicates_sorted():
    """Provide sorted data with duplicates for testing"""
    return [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]