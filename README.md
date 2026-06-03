# Sparse Array in Python 🐍

A memory-efficient 1D Sparse Array implementation in Python utilizing Python's Magic Methods (`__getitem__`, `__setitem__`, `__delitem__`, and more).

## 💡 What is a Sparse Array?
In computer science, a sparse array is an array in which most of the elements have a value of zero (or a default value). Storing all those zeros in a traditional list wastes memory. 

This implementation uses a Python dictionary (`dict`) under the hood to **only store non-zero values**, significantly optimizing memory usage while preserving the behavior of a standard list.

## 🚀 Features & Implemented Magic Methods

- **Memory Efficiency**: Only non-zero elements occupy actual memory.
- **`__len__`**: Returns the virtual length of the array, including the zeros.
- **`__getitem__` & `__setitem__`**: Supports standard bracket indexing (e.g., `arr[3] = 10` or `print(arr[3])`).
- **`__delitem__`**: Allows deleting elements using `del arr[index]`, automatically shifting all subsequent indices to the left.
- **`append()`**: Dynamically grows the virtual array length.
- **`__contains__`**: Supports the `in` operator (e.g., `if 7 in arr:`), with smart logic to detect virtual zeros.
- **`__add__`**: Concatenates two `SparseArray` objects together (`arr1 + arr2`).
- **`__lt__` & `__gt__`**: Compares two arrays based on their virtual length.
- **`__repr__`**: Pretty-prints the array structure so it looks like a native Python list in the console.

## 🛠️ Usage Example

```python
from main import SparseArray

# Create a sparse array with lots of zeros
arr = SparseArray([0, 7, 0, 5, 0])

# Access and modify elements
print(arr[1])  # Output: 7
arr[2] = 9     # Modifies the array efficiently

# Delete an item (subsequent items will shift left)
del arr[1] 

# Append new data
arr.append(12)

print(arr)  # Output: [0, 9, 5, 0, 12]