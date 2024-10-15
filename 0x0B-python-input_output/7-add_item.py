#!/usr/bin/python3
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Try to load existing list from the file, if it exists
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Check if any arguments are provided
if len(sys.argv) > 1:
    # Add all arguments (except the script name) to the list
    items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)

