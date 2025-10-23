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
def empty_array():
    """Provide empty array for testing"""
    return []

@pytest.fixture
def single_element_array():
    """Provide single element array for testing"""
    return [42]

@pytest.fixture
def data_with_duplicates_unsorted():
    """Provide unsorted data with duplicates for testing"""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

@pytest.fixture
def data_with_duplicates_sorted():
    """Provide sorted data with duplicates for testing"""
    return [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]

@pytest.fixture
def data_with_negative_numbers_unsorted():
    """Provide unsorted data with negative numbers for testing"""
    return [-7, -2, -9, -4, -1, -8, -3, -10, -5, -6]

@pytest.fixture
def data_with_negative_numbers_sorted():
    """Provide sorted data with negative numbers for testing"""
    return [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

@pytest.fixture
def data_with_floats_unsorted():
    """Provide unsorted data with floats for testing"""
    return [3.14, 2.71, 1.41, 1.73]

@pytest.fixture
def data_with_floats_sorted():
    """Provide sorted data with floats for testing"""
    return [1.41, 1.73, 2.71, 3.14]

@pytest.fixture
def data_with_strings_unsorted():
    """Provide unsorted data with strings for testing"""
    return ["banana", "apple", "cherry", "date"]

@pytest.fixture
def data_with_strings_sorted():
    """Provide sorted data with strings for testing"""
    return ["apple", "banana", "cherry", "date"]