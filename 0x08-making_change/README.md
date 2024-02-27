# 0-making_change.py 📖

## Description ⚙️
The "Making Change" project is a task that involves solving the classic coin change problem. The objective is to find the fewest number of coins required to make up a given total amount, given a list of coin denominations. The project challenges you to apply your understanding of greedy algorithms and dynamic programming to devise a solution that is not only correct but also efficient.

## Concepts Covered
- **Greedy Algorithms:**
  - Understanding how greedy algorithms work and their suitability for the coin change problem.
  - Recognizing the limitations of greedy algorithms and scenarios where they might not provide the optimal solution.
- **Dynamic Programming:**
  - Basic principles of dynamic programming as a method to solve optimization problems.
  - The concept of overlapping subproblems and optimal substructure in the context of the coin change problem.
- **Algorithmic Complexity:**
  - Analyzing the time and space complexity of algorithms.
  - Striving for solutions with lower complexity to meet runtime constraints.
- **Problem-Solving Strategies:**
  - Breaking down the problem into smaller, manageable sub-problems.
  - Iterative vs recursive approaches to dynamic programming.
- **Python Programming:**
  - Manipulating lists and using list comprehensions.
  - Implementing functions with efficient looping and conditional statements.

## Requirements
- **General:**
  - Allowed editors: vi, vim, emacs.
  - All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3).
  - All files should end with a new line.
  - The first line of all files should be exactly `#!/usr/bin/python3`.
  - A `README.md` file, at the root of the project folder, is mandatory.
  - Your code should use the PEP 8 style (version 1.7.x).
  - All your files must be executable.

## Tasks
### 0. Change comes from within
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

- **Prototype:** `def makeChange(coins, total)`
- **Return:** Fewest number of coins needed to meet the total.
- If the total is 0 or less, return 0.
- If the total cannot be met by any number of coins you have, return -1.
- `coins` is a list of the values of the coins in your possession.
- The value of a coin will always be an integer greater than 0.
- You can assume you have an infinite number of each denomination of coin in the list.
- Your solution’s runtime will be evaluated in this task.

**Example Usage:**
```python
makeChange([1, 2, 25], 37)  # Output: 7
makeChange([1256, 54, 48, 16, 102], 1453)  # Output: -1
```
