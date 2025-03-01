# Python Memory Management & Garbage Collection

This document explores Python’s memory management, reference counting, and garbage collection through small test scripts.

##  Memory Usage of Different Data Structures

```python
import sys

a = [1, 2, 3, 4, 5]
b = (1, 2, 3, 4, 5)
c = {"name": "Alice", "age": 25}

print("List size:", sys.getsizeof(a))
print("Tuple size:", sys.getsizeof(b))
print("Dictionary size:", sys.getsizeof(c))
```

### Output:
```
List size: 104
Tuple size: 80
Dictionary size: 184
```

### Explanation:
- **List:** Stores elements in dynamic arrays, with extra space to allow appending elements.
- **Tuple:** Immutable and more memory-efficient than lists.
- **Dictionary:** Stores key-value pairs, with extra space for hashing and fast lookups.

---

##  Garbage Collection and `__del__` Destructor

```python
import gc

class Test:
    def __del__(self):
        print("Object deleted!")

obj = Test()
del obj
gc.collect()
```

### Output:
```
Object deleted!
0
```

### Explanation:
- **Destructor:** When the object is deleted with `del`, Python calls the `__del__` method.
- **Garbage Collection:** `gc.collect()` forces garbage collection, but returns `0` because no cyclic references were present.

---

##  Reference Counting

```python
import sys

a = [1, 2, 3]
b = a

print("Reference count of a:", sys.getrefcount(a))

del a

print("Reference count after deleting a:", sys.getrefcount(b))
```

### Output:
```
Reference count of a: 3
Reference count after deleting a: 2
```

### Explanation:
- **Reference Counting:** `sys.getrefcount()` returns the number of references to an object.
- **Increment & Decrement:** `b = a` increases the reference count. After `del a`, `b` still holds a reference.

---

##  Python Garbage Collection Example

This script demonstrates Python's automatic garbage collection, especially how it handles circular references using the `gc` module.

```python
import gc

class Test:
    def __del__(self):
        print("Object deleted!")

a = Test()
b = Test()
a.ref = b
b.ref = a

del a
del b

collected = gc.collect()

print("Number of objects collected:", collected)
```

### Output:
```
Object deleted!
Object deleted!
Number of objects collected: 8
```

### Explanation:
1. **Class with a Destructor:** The `Test` class has a `__del__` method to print when an object is deleted.
2. **Circular Reference:** Two instances (`a` and `b`) reference each other, forming a cycle.
3. **Manual Deletion:** `del a` and `del b` remove the names, but the objects still exist in memory due to the circular reference.
4. **Garbage Collection:** `gc.collect()` forces Python’s garbage collector to run, breaking the cycle and freeing memory.

---

##  Key Takeaways
- **Memory Efficiency:** Lists, tuples, and dictionaries have different memory footprints.
- **Reference Counting:** Python uses reference counting as the primary memory management mechanism.
- **Garbage Collection:** The garbage collector cleans up cyclic references.
- **Manual Collection:** Use `gc.collect()` to manually trigger collection when necessary.

