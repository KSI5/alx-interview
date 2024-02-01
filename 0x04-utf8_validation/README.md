#   0x04-utf8_validation

This project contains a Python method `validUTF8` that determines if a given data set represents a valid UTF-8 encoding.

## Prototype

```python
def validUTF8(data)
```

## Return

- `True` if data is a valid UTF-8 encoding.
- `False` if data is not a valid UTF-8 encoding.

## Requirements

- A character in UTF-8 can be 1 to 4 bytes long.
- The data set can contain multiple characters.
- The data will be represented by a list of integers.
- Each integer represents 1 byte of data; therefore, you only need to handle the 8 least significant bits of each integer.

## Examples

```python
data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
```

## Files

- The Python script containing the `validUTF8` method: [0-validate_utf8.py](0x04-utf8_validation/0-validate_utf8.py)
- The main script for testing: [0-main.py](0x04-utf8_validation/0-main.py)
``
