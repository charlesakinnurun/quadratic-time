<!-- # Quadratic‑Time

**Explanation of Quadratic Time Complexity (O(n²))**

This repository provides examples and explanations related to **quadratic time complexity**, often written as **O(n²)** — a type of algorithmic complexity where the running time grows proportionally to the *square* of the input size.

---

## 📊 What Is Quadratic Time (O(n²))?

In algorithm analysis, **quadratic time complexity** means that the time an algorithm takes grows roughly with the square of the input size. This typically happens when an algorithm uses **nested loops** — that is, a loop inside another loop — where each element of the input is processed against every other element.



---

## 📌 Common Examples of O(n²) Algorithms

Algorithms and operations that often run in quadratic time include:

- **Nested loop comparisons:** like printing all pairs of elements in a list.
- **Simple sorting algorithms:** such as **Bubble Sort**, **Insertion Sort**, and **Selection Sort** in their basic forms. 
- **Matrix operations:** like filling or traversing a two‑dimensional square matrix. 

---

## 📁 Source Code
```python
"""
UNDERSTANDING QUADRATIC TIME COMPLEXITY O(n^2)

Quadratic time complexity occurs when the time it takes to complete a task 
is proportional to the square of the input size (n). In big-O notation, 
this is written as O(n^2).

Common scenarios for O(n^2):
1. Nested loops: An outer loop running 'n' times containing an inner loop 
   that also runs 'n' times.
2. Comparing every element in a list with every other element.
"""

import time
import random


def bubble_sort(data):
    """
    Bubble Sort is a classic example of an O(n^2) algorithm.
    It uses two nested loops to sort a list.
    """
    n = len(data)

    # The outer loop runs "n" times
    for i in range(n):
        # The inner loop runs "n" times for every iteration of the outer loop
        # n * n = n^2
        for j in range(0, n - i - 1):
            # Th is comparison happens n^2 times in the worst casde
            if data[j] > data[j + 1]:
                # Swapping elements
                data[j], data[j + 1] = data[j + 1], data[j]
    return data




def demonstrate_complexity():
    # We will test the algorithm with three different input sizes
    # to see how the increases quadratically
    sizes = [100,500,1000]

    print(f"{"Input Size (n)": <20} | {"Time taken (seconds)"}:<20")
    print("-" * 45)

    for size in sizes:
        # Generate a random list of "n" inntegers
        test_list = [random.randint(0,1000) for _ in range(size)]

        # Record the start time
        start_time = time.time()

        # Execute the O(n^2) algorithm
        bubble_sort(test_list)

        # Record the end time
        end_time = time.time()
        duration = end_time - start_time

        print(f"{size:<20} | {duration:<20.5f}")



if __name__ == "__main__":
    print("Starting O(n^2) Demonstration...")
    print("Notice how doubling the input size (500 to 1000) roughly")
    print("quadruples the time taken (2^2 = 4).\n")
    
    demonstrate_complexity()
    
    print("\nSummary:")
    print("- If n = 10, operations = 100")
    print("- If n = 100, operations = 10,000")
    print("- If n = 1000, operations = 1,000,000")
    print("This steep growth is why O(n^2) algorithms are often avoided for large datasets.")
```

---

## 🧠 Why It Matters

Quadratic algorithms are **simple to understand and implement**, and they can work well for small input sizes. However, as the size of the input grows, the performance **deteriorates quickly** because the number of operations increases much faster than linear or logarithmic algorithms.



-->



<!-- # 📘 Quadratic Time – README -->

<h1 align="center"> Quadratic Time</h1>

## Overview

**Quadratic Time** refers to an algorithm whose runtime grows proportional to the square of the input size.

If the input size doubles, the running time roughly quadruples.

In algorithm analysis, this is expressed as:

```
O(n²)
```

Quadratic time is common in algorithms with nested loops over the input.

<a href="/src/main.py">Check out for source code</a>

---

## ⚙️ What Quadratic Time Means

An algorithm runs in quadratic time when it must perform a number of operations proportional to n × n, often because it compares every element with every other element.

Common examples:

* Bubble Sort
* Selection Sort
* Checking all pairs in an array
* Brute-force algorithms

For an input array of n elements, the algorithm performs approximately n² steps.

---

## 🧠 Python Examples

### Example 1 — Bubble Sort

```python id="bs2a0c"
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


numbers = [5, 3, 8, 4, 2]
print(bubble_sort(numbers))
```

Nested loops → **O(n²)** time.

---

### Example 2 — Pair Sum Check

```python id="ps9f2x"
def has_pair_with_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False


arr = [1, 2, 3, 4, 5]
print(has_pair_with_sum(arr, 9))  # True (4+5)
```

Every pair is checked → **O(n²)** time.

---

### Example 3 — Selection Sort

```python id="ss5x8q"
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


numbers = [64, 25, 12, 22, 11]
print(selection_sort(numbers))
```

Nested comparison loops → **O(n²)** time.

---

## ⏱️ Time Complexity Comparison

| Complexity | Meaning           |
| ---------- | ----------------- |
| O(1)       | Constant time     |
| O(n)       | Linear time       |
| O(n log n) | Linearithmic time |
| **O(n²)**  | Quadratic time    |
| O(n³)      | Cubic time        |

Quadratic algorithms become very slow as input size grows.

---

## 👍 Advantages

* Simple and easy to implement
* Works fine for small datasets
* Conceptually intuitive for learning algorithms

## 👎 Disadvantages

* Very inefficient for large datasets
* Performance grows rapidly as n increases
* Often replaced by more efficient algorithms (O(n log n))

---

## 📌 When Quadratic Time Occurs

Quadratic time operations typically appear in:

* Nested loops iterating over arrays
* Bubble Sort, Selection Sort, Insertion Sort (worst-case)
* Brute-force pair checking
* Comparing all items with each other

---

## 🏁 Summary

Quadratic time complexity **O(n²)** occurs when an algorithm has nested iterations over the input.
While acceptable for small inputs, it becomes impractical for large datasets, and more efficient algorithms are preferred.

