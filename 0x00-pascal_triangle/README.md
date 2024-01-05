
# Pascal's Triangle

## Overview
This Python script generates Pascal's Triangle up to a specified number of rows `n` and returns the result as a list of lists of integers.

## Function Description
```python
def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to row n.

    Args:
        n (int): Number of rows.

    Returns:
        list of lists of integers: Pascal's Triangle.
    """
    # Function implementation
If n is less than or equal to 0, the function returns an empty list.
Otherwise, it iteratively builds each row of Pascal's Triangle using the previous row.
