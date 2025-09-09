# Mindbox_Code_Challenge_2
# Mindbox Code Challenge: Geometric Shapes Library

A Python library for calculating the areas of geometric shapes.  
Designed with **polymorphism** and **extensibility** in mind.

---

## Features

- **Area Calculation**  
  - Circle: area by radius  
  - Triangle: area by three sides  

- **Polymorphism**  
  Calculate area without knowing the figure type at compile time.  

- **Extensibility**  
  Easily add new shapes without modifying existing code.  

- **Right-Angled Triangle Check**  
  `Triangle` class includes a method to check if a triangle is right-angled.  

- **Unit Tests**  
  Covered with `pytest` for reliability.  

---

## How to Run

### 1. Requirements
- Python `3.12.0`  
- `pytest`

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run tests
```bash
pytest
```
