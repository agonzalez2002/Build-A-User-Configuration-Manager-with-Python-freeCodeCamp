# User Configuration Manager - Python

A simple Python program built for **freeCodeCamp's 'Build a User Configuration Manager' for Python Certification**. It manages a user settings dictionary by providing basic CRUD (Create, Read, Update, Delete) operations.

## What This Code Does

* **Add Setting:** Adds a new key-value pair if the key doesn't already exist.
* **Update Setting:** Modifies an existing key's value.
* **Delete Setting:** Removes a setting from the dictionary.
* **View Settings:** Formats and prints all active settings cleanly.

## Python Concepts Used

* **Dictionary Operations:** Adding, updating, checking membership (`in`), deleting (`del`), and iterating over items (`.items()`).
* **Tuple Unpacking:** Extracting `key, value` pairs from input tuples.
* **String Manipulation:** Standardizing text with `.lower()`, `.capitalize()`, and joining lines with `"\n".join()`.
* **Control Flow:** Using `if/else` statements to check if settings exist before modifying them.

## How to Run

1. Clone or download this repository.
2. Run the script in your terminal:
   ```bash
   python main.py
   ```
