# Python List Comprehensions & Lambda Functions

This document explains Python's powerful features: **list comprehensions** and **lambda functions**

---

##  **List Comprehensions**
List comprehensions provide a concise way to create lists. They make your code more readable and Pythonic.

###  **Basic Example:**
```python
nums = [1, 2, 3, 4, 5]

# Without list comprehension
squared = []
for n in nums:
    squared.append(n * n)

# With list comprehension
squared = [n * n for n in nums]
```

 **Output:** `[1, 4, 9, 16, 25]`

---

###  **Examples:**

1. **Double elements in a list:**
```python
nums = [1, 2, 3]
doubled = [n * 2 for n in nums]
```

2. **Filter even numbers:**
```python
even_nums = [n for n in nums if n % 2 == 0]
```

3. **Create pairs of elements:**
```python
pairs = [(letter, num) for letter in 'abcd' for num in range(4)]
```

4. **Dictionary comprehension:**
```python
names = ['Bruce', 'Clark', 'Peter']
heros = ['Batman', 'Superman', 'Spiderman']
hero_dict = {name: hero for name, hero in zip(names, heros)}
```

5. **Set comprehension:**
```python
nums = [1, 1, 2, 3, 3]
unique_nums = {n for n in nums}
```

---

##  **Lambda Functions**
Lambda functions are small, anonymous functions defined with the `lambda` keyword. They're useful for short, throwaway functions.

###  **Basic Example:**
```python
# Regular function
def square(n):
    return n * n

# Lambda function
square = lambda n: n * n
```

 **Output:** `square(5)` → `25`

---

###  **Examples:**

1. **Double a number:**
```python
multiply = lambda a, b: a * b
```

2. **Filter even numbers with `filter`:**
```python
nums = [1, 2, 3, 4]
even_nums = list(filter(lambda n: n % 2 == 0, nums))
```

3. **Square numbers with `map`:**
```python
squared = list(map(lambda n: n * n, nums))
```

4. **Sort a list of tuples by the second element:**
```python
pairs = [(1, 3), (2, 2), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
```

---

##  **Takeaways:**
- **List comprehensions** simplify list creation and transformations.
- **Lambda functions** are great for short, one-off functions.
- **Higher-order functions** like `map`, `filter`, and `sorted` work well with lambdas.
