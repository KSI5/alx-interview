#!/usr/bin/python3
"""
Minimum Operations Module
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Args:
        n (int): Number of H characters to achieve.

    Returns:
        int: Fewest number of operations needed.

    Notes:
        If n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

if __name__ == "__main__":
    # Example usage
    n1 = 4
    print("Min # of operations to reach {} char: {}".format(n1, minOperations(n1)))

    n2 = 12
    print("Min # of operations to reach {} char: {}".format(n2, minOperations(n2)))
