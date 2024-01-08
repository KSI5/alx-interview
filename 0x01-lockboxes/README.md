# Lockboxes Challenge

## Overview

This Python script provides a method to determine if all boxes can be opened in a set of locked boxes. Each box is numbered sequentially, and each box may contain keys to other boxes. The goal is to check if it's possible to unlock all the boxes.

## Method

The script defines a function `canUnlockAll(boxes)` that takes a list of lists as input. Each sublist represents a box, and the keys inside the sublist indicate the boxes that can be opened. The function returns `True` if all boxes can be opened, and `False` otherwise.

## Example

```python
#!/usr/bin/python3

from lockboxes import canUnlockAll

# Example 1
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

# Example 2
boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

# Example 3
boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/KSI5/alx-interview.git


2. Navigate to the project directory:
   ```bash
   cd your-repository/0x01-lockboxes
   ```

3. Run the script:
   ```bash
   ./main_0.py
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
