# 0x02-minimum Operations 📝

This Python script calculates the fewest number of operations needed to achieve a specific number of 'H' characters in a text file. The allowed operations are 'Copy All' and 'Paste.'

## Requirements 🛠️

- Editors: vi, vim, emacs
- Interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- PEP 8 style (version 1.7.x)
- All files must be executable

## Usage 🚀

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/alx-interview.git
   ```

2. Navigate to the project directory:

   ```bash
   cd alx-interview/0x02-minimum_operations
   ```

3. Run the main script:

   ```bash
   ./0-main.py
   ```

4. View the minimum number of operations required for different scenarios.

## Example 📚

```python
n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

## Function Documentation 📖

### `minOperations(n)`

Calculates the fewest number of operations needed to result in exactly n 'H' characters in the file.

#### Parameters:

- `n` (int): Number of 'H' characters to achieve.

#### Returns:

- `int`: Fewest number of operations needed.

#### Notes:

If n is impossible to achieve, return 0.

## Author 🧑‍💻

Christopher Igebu
