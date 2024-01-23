# 0-stats.py

This script reads input from stdin line by line, parsing log entries, and computes various metrics. It prints statistics after every 10 lines or when interrupted with CTRL + C.



## Usage

Run the script and provide log entries as input. Statistics will be printed after every 10 lines or when the script is interrupted.

```bash
python log_parser.py < access.log
```

## Statistics

After every 10 lines and/or interruption, the script prints the following statistics:

1. **Total File Size:** The sum of all previous file sizes.

2. **Number of Lines by Status Code:** Displays the count for each status code.

   - Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500.
   - If a status code doesn't appear or is not an integer, it won't be included in the output.

   Example:

   ```
   200: 5
   404: 3
   ```

Status codes are printed in ascending order.

## Example

```bash
python log_parser.py < access.log
```

## Requirements

- Python 3

## Notes

- Ensure that the log entries adhere to the specified format for accurate parsing.
- If there are fewer than 10 lines, statistics won't be printed until 10 lines are reached.
