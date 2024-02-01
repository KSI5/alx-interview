#!/usr/bin/python3
"""
Module for UTF-8 Validation
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): List of integers representing the data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False.
    """

    # Helper function to check if a byte is a valid start of a UTF-8 character
    def is_start_of_char(byte):
        return bin(byte).count('1') == 1

    # Helper function to check if the next bytes in the sequence are valid
    def is_valid_sequence(start, data):
        for i in range(start + 1, start + min(4, len(data) - start)):
            if i >= len(data) or (data[i] >> 6) != 0b10:
                return False
        return True

    i = 0
    while i < len(data):
        if data[i] < 128:
            i += 1
        elif data[i] >> 5 == 0b110 and is_valid_sequence(i, data):
            i += 2
        elif data[i] >> 4 == 0b1110 and is_valid_sequence(i, data):
            i += 3
        elif data[i] >> 3 == 0b11110 and is_valid_sequence(i, data):
            i += 4
        else:
            return False

    return True

# Example usage
if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))  # Output: True

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))  # Output: True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # Output: False
