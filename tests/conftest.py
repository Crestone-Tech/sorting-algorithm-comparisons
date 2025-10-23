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

