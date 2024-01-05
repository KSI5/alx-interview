def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to row n.

    Args:
        n (int): Number of rows.

    Returns:
        list of lists of integers: Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle

# Example usage:
if __name__ == "__main__":
    # Example from your provided main script
    result = pascal_triangle(5)
    for row in result:
        print(row)
