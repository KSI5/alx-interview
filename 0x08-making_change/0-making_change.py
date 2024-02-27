#!/usr/bin/python3
"""
Module for making change problem
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    # Initialize a table to store results of subproblems
    # table[i] will be storing the minimum number of coins needed for i value
    table = [float('inf')] * (total + 1)

    # Base case (if given value is 0)
    table[0] = 0

    # Compute the minimum number of coins needed for all values from 1 to total
    for i in range(1, total + 1):
        # Go through all coins and update the table value
        for coin in coins:
            if coin <= i:
                subproblem = table[i - coin]
                if subproblem != float('inf') and subproblem + 1 < table[i]:
                    table[i] = subproblem + 1

    # If table[total] is still infinite, then total can't be reached
    if table[total] == float('inf'):
        return -1

    return table[total]

# Example usage
if __name__ == "__main__":
    coins_1 = [1, 2, 25]
    total_1 = 37
    print(makeChange(coins_1, total_1))  # Output: 7

    coins_2 = [1256, 54, 48, 16, 102]
    total_2 = 1453
    print(makeChange(coins_2, total_2))  # Output: -1
