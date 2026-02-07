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