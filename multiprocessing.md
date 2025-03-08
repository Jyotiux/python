## Understanding CPU-bound and I/O-bound Tasks with Python Multiprocessing and Concurrent Futures

### Introduction
Parallel processing can dramatically speed up your programs, especially for CPU-bound or I/O-bound tasks. In this document, we'll break down how Python's `multiprocessing` and `concurrent.futures` libraries help handle these tasks. Let’s explore with examples and explanations!

---

## CPU-bound vs I/O-bound Tasks

- **CPU-bound tasks:** Heavy computation tasks where the CPU is the bottleneck (e.g., image processing, matrix operations).
- **I/O-bound tasks:** Waiting for external events like file I/O or network requests (e.g., downloading data, reading files).

Python’s Global Interpreter Lock (GIL) limits concurrency for CPU-bound tasks, but `multiprocessing` or `ProcessPoolExecutor` can bypass it by using separate processes.

---

## Basic Example: `multiprocessing.Process`

```python
import multiprocessing
import time
start = time.perf_counter()

def do_something():
    print('Sleeping 1 second')
    time.sleep(1)
    print('Done Sleeping')

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
```

### Explanation:
- **Without multiprocessing:** Two tasks would take ~2 seconds.
- **With multiprocessing:** Tasks run in parallel, finishing in ~1 second.

---

## Using `concurrent.futures.ProcessPoolExecutor`

```python
import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
```

### Explanation:
- **`ProcessPoolExecutor`:** Manages a pool of worker processes.
- **`executor.map`:** Maps the function across multiple inputs, running them in parallel.

---

## Image Processing Example (CPU-bound)

```python
import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = ['image1.jpg', 'image2.jpg', 'image3.jpg']

t1 = time.perf_counter()

size = (1200, 1200)

def process_image(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')

with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names)

t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')
```

### Explanation:
- **CPU-bound task:** Applying a Gaussian blur and resizing images.
- **Parallel execution:** Each image processes independently, speeding up the workflow.

---

## Key Takeaways

1. **Multiprocessing:** Ideal for CPU-bound tasks, bypassing GIL.
2. **ProcessPoolExecutor:** Simplifies process management.
3. **Concurrency vs Parallelism:** Concurrency is about dealing with many tasks at once; parallelism is about doing many tasks simultaneously.


