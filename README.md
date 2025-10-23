# Sorting Algorithm Comparisons

A comprehensive system for comparing sorting algorithms with performance instrumentation, REST API, and interactive visualization.

## Project Structure

```
sorting-algorithm-comparisons/
├── src/                    # Source code
│   ├── algorithms/        # Sorting algorithm implementations
│   ├── api/              # FastAPI application
│   ├── instrumentation/  # Performance measurement tools
│   └── utils/            # Utility functions
├── tests/                 # Test suite
├── ui/                    # Frontend (coming soon)
└── docs/                  # Documentation
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. For development, install dev dependencies:
```bash
pip install -r requirements-dev.txt
```

## Running the API

```bash
uvicorn src.api.main:app --reload
```

The API will be available at http://localhost:8000

API documentation will be available at http://localhost:8000/docs

## Running Tests

```bash
pytest
```

## Project Status

🚧 This project is currently under development.

---

## Project Plan

### Phase 1: Core Infrastructure & API Foundation
1. **Project Structure Setup**
   - ✅ Create modular Python package structure
   - Set up virtual environment and dependency management
   - Configure logging and configuration management

2. **Sorting Algorithm Implementations**
   - Implement core sorting algorithms (Bubble Sort, Quick Sort, Merge Sort, Heap Sort, Insertion Sort, Selection Sort)
   - Add instrumentation hooks for performance measurement (execution time, memory usage, comparisons, swaps)
   - Create abstract base class for consistent algorithm interface

3. **API Development**
   - Build FastAPI-based REST API
   - Endpoints for:
     - `/sort` - Execute sorting with algorithm selection and data input
     - `/algorithms` - List available sorting algorithms
     - `/performance` - Get performance metrics for specific runs
     - `/health` - API health check

4. **Data Management**
   - Input validation for sorting data
   - Support for different data types (integers, floats, strings)
   - Data generation utilities for testing (random, sorted, reverse-sorted, nearly-sorted)

### Phase 2: Testing & Validation
5. **Automated Testing Suite**
   - Unit tests for each sorting algorithm
   - Integration tests for API endpoints
   - Performance regression tests
   - Test data generation and validation

6. **API Testing Framework**
   - Comprehensive test coverage for all endpoints
   - Load testing for performance validation
   - Error handling and edge case testing

### Phase 3: User Interface & Visualization
7. **Web UI Development**
   - Modern, responsive frontend (React/Vue.js or Flask templates)
   - Interactive algorithm selection interface
   - Real-time performance visualization
   - Data input and customization options

8. **Visualization Components**
   - Performance comparison charts (execution time, memory usage)
   - Algorithm efficiency graphs
   - Interactive sorting process visualization
   - Export capabilities for results
