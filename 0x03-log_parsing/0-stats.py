#!/usr/bin/python3
import sys

def print_stats(total_size, status_counts):
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))

def parse_line(line):
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except (ValueError, IndexError):
        return None

def main():
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            parsed_line = parse_line(line.strip())
            if parsed_line:
                ip_address, status_code, file_size = parsed_line
                total_size += file_size
                status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if i % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        pass  # Handle Ctrl+C

    print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
