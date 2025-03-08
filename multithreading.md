# Speeding Up Code with Concurrent Execution in Python

## Basic Sequential Execution

```python
import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second(s)...')
    time.sleep(1)
    return 'Done Sleeping'

do_something()
do_something()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
```
**Output:**
```
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Finished in 2.0 second(s)
```

## Parallel Execution with Threads (Without Join)

```python
import threading
import time

start = time.perf_counter()

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
```
**Output (incorrect timing due to missing join):**
```
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Finished in 0.0 second(s)
```

## Using `join` to Wait for Threads

```python
start = time.perf_counter()

t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
```
**Correct Output:**
```
Sleeping 1 second(s)...
Sleeping 1 second(s)...
Finished in 1.0 second(s)
```

## Scaling Up with Multiple Threads

```python
threads = []

for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
```
**Output:**
```
Sleeping 1 second(s)... (10 times)
Finished in 1.0 second(s)
```

## Passing Arguments to Threads

```python
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping {seconds} second(s)'

threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
```
**Output:**
```
Sleeping 1.5 second(s)... (10 times)
Finished in 1.5 second(s)
```

## Using ThreadPoolExecutor

```python
import concurrent.futures

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_something, 1) for _ in range(10)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
```

## Using `map` with ThreadPoolExecutor

```python
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)
```

## Downloading Images with Threads

```python
import requests

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    # Add more URLs...
]

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)
```
**Output:**
```
photo-1516117172878-fd2c41f4a759.jpg was downloaded...
photo-1532009324734-20a7a5813719.jpg was downloaded...
Finished in X seconds
```
