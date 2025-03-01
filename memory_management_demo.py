# Python Memory Management Demo
# ------------------------------
# Author: Jyoti Singh
# Date: 1 March 2025
# Description: A collection of small scripts demonstrating Python's memory management concepts.

# Section 1: Object Sizes
import sys
a = [1, 2, 3, 4, 5]
b = (1, 2, 3, 4, 5)
c = {"name": "Alice", "age": 25}
print("List size:", sys.getsizeof(a))  # List size: 104
print("Tuple size:", sys.getsizeof(b))  # Tuple size: 80
print("Dictionary size:", sys.getsizeof(c))  # Dictionary size: 184

# Section 2: Object Deletion & Garbage Collection
import gc
class Test:
    def __del__(self):
        print("Object deleted!")

obj = Test()
del obj  # Object deleted!
gc.collect()  # 0

# Section 3: Reference Counting
a = [1, 2, 3]
b = a
print("Reference count of a:", sys.getrefcount(a))  # 3
del a
print("Reference count after deleting a:", sys.getrefcount(b))  # 2

# Section 4: Circular References
class Test:
    def __del__(self):
        print("Object deleted!")

g = Test()
h = Test()
g.ref = h
h.ref = g
del g
del h
collected = gc.collect()
print("Number of objects collected:", collected)
