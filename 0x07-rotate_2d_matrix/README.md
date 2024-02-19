# 0-rotate_2d_matrix.py

This Python script is designed to rotate an n x n 2D matrix 90 degrees clockwise in-place.

## Prototype

```python
def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list[list[int]]): The input matrix to be rotated.

    Returns:
        None. The matrix is modified in-place.

    Example:
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

        rotate_2d_matrix(matrix)
        print(matrix)

    Output:
        [[7, 4, 1],
         [8, 5, 2],
         [9, 6, 3]]
```

## Usage

To use this script, follow these steps:

1. Import the `rotate_2d_matrix` function:

    ```python
    from 0-rotate_2d_matrix import rotate_2d_matrix
    ```

2. Create a 2D matrix to rotate:

    ```python
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    ```

3. Call the `rotate_2d_matrix` function:

    ```python
    rotate_2d_matrix(matrix)
    ```

4. Print the rotated matrix:

    ```python
    print(matrix)
    ```

## Example

```python
from 0-rotate_2d_matrix import rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
```

Output:

```python
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```

## Repository Information

**GitHub Repository:** [alx-interview](https://github.com/KSI5/alx-interview)

**Directory:** 0x07-rotate_2d_matrix

**File:** 0-rotate_2d_matrix.py
