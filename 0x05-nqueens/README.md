# 0-nqueens.py 🕹️

## Overview 🚀

This Python program is a solver for the N-Queens problem – the challenge of placing N non-attacking queens on an N×N chessboard.

## Usage 🤖

To use the program, run the following command in your terminal:

```bash
./0-nqueens.py N
```

- `N` must be an integer greater than or equal to 4.
- If called with the wrong number of arguments, it will print `Usage: nqueens N` and exit with status 1.
- If `N` is not an integer, it will print `N must be a number` and exit with status 1.
- If `N` is smaller than 4, it will print `N must be at least 4` and exit with status 1.

The program will print every possible solution to the N-Queens problem, with one solution per line.

## Example 🎲

```bash
./0-nqueens.py 4
```

Output:
```python
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## Repository 📂

- **GitHub Repository:** [alx-interview](https://github.com/KSI5/alx-interview)
- **Directory:** 0x05-nqueens
- **File:** 0-nqueens.py