# 1# namedtuple----------------------------------------------


# from collections import namedtuple  # Import namedtuple factory from the collections module

# # Create a named tuple type called 'User' with 4 fields: user, username, email, pw
# User = namedtuple("User", "user username email pw")

# print(type(User))  
# # This prints: <class 'type'>
# # 'User' itself is a class that was created by namedtuple()

# # Create an instance of the namedtuple
# someone = User("Bill", "billy", "billy@gmail.com", "1234")

# # The below line just shows what a User tuple looks like (not actually printed)
# User(user='Bill', username='billy', email='billy@gmail.com', pw='1234')

# # Access by index
# print(someone[0])  
# # Output: Bill

# # Access by field name
# print(someone.user)  
# # Output: Bill

# # Convert to a dictionary (field_name → value)
# print(someone._asdict())  
# # Output: {'user': 'Bill', 'username': 'billy', 'email': 'billy@gmail.com', 'pw': '1234'}

# # _replace() creates a **new** namedtuple with one or more fields replaced
# someone._replace(pw='3456')

# # The above line does NOT modify the existing tuple (since namedtuples are immutable)
# # It returns a new object — but you didn’t assign it to a variable, so it’s discarded

# print(someone)
# # Output: User(user='Bill', username='billy', email='billy@gmail.com', pw='1234')
# # The password remains '1234' because the _replace() result wasn’t saved



#2 # ---------------------------------------------
# # deque — a double-ended queue (list-like structure)
# # It allows appending and popping elements efficiently from both ends.
# # ---------------------------------------------

# from collections import deque  # Import deque from the collections module

# x = deque([1, 2, 3])           # Create a deque initialized with elements [1, 2, 3]
# print(x)                       # Output: deque([1, 2, 3])

# x.appendleft([6])              # Add [6] (a list as one element) to the *left* end
# print(x)                       # Output: deque([[6], 1, 2, 3])

# x.popleft()                    # Remove and return the *leftmost* element ([6])
# print(x)                       # Output: deque([1, 2, 3])

# x.rotate()                     # Rotate right by 1 (default is +1)
#                                # This moves the last element to the front
# print(x)                       # Output: deque([3, 1, 2])

# x.rotate(1)                    # Rotate again right by 1
# print(x)                       # Output: deque([2, 3, 1])

# x.rotate()                     # Another rotate right by 1
# print(x)                       # Output: deque([1, 2, 3])

# x.rotate(2)                    # Rotate right by 2 (move last two elements to front)
# print(x)                       # Output: deque([2, 3, 1])

# # Now using deque with a fixed maximum length
# x = list(range(10))            # Create a normal list [0, 1, 2, ..., 9]
# print(x)                       # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# x = deque(x, 5)                # Create a deque with maxlen=5 from that list
#                                # Keeps only the *last 5 elements* -> [5, 6, 7, 8, 9]
# print(x)                       # Output: deque([5, 6, 7, 8, 9], maxlen=5)

# # New deque without maxlen
# x = deque([30, 40, 50])
# x.append(60)                   # Append 60 to the right end
# print(60)                      # Prints the number 60 (not deque contents)
# x.appendleft(70)               # Append 70 to the left end
# print(x)                       # Output: deque([70, 30, 40, 50, 60])




# # 3---------------------------------------------
# # defaultdict — a dictionary subclass that provides default values
# # for keys that don't exist yet.
# # ---------------------------------------------

# from collections import defaultdict  # Import defaultdict from the collections module

# # Create a defaultdict where each missing key has a default value of 0 (int() → 0)
# dice = defaultdict(int)
# print(dice)  # Initially empty: defaultdict(<class 'int'>, {})

# # Accessing keys that don't exist yet automatically creates them with default value 0
# for i in range(2, 13):         # Typical range for dice sums (2–12)
#     print(dice[i])             # Prints 0 for each, since no values assigned yet


# # Example 2: Grouping data using defaultdict(list)


# import random

# # Lists of names and countries to randomly choose from
# names = ["Liam", "Olivia", "Noah", "Ema"]
# countries = ["US", "UK", "China", "Russia"]

# # Create a list of 25 random (country, name) pairs
# data = [(random.choice(countries), random.choice(names)) for i in range(25)]
# print(data)  # Example: [('UK', 'Liam'), ('US', 'Ema'), ('China', 'Noah'), ...]

# # Create a defaultdict where each missing key automatically gets an empty list []
# grouped = defaultdict(list)

# # Loop through each (country, name) pair and group names by country
# for country, name in data:
#     grouped[country].append(name)  # Append the name to that country's list

# # Print the grouped result
# print(grouped)
# # Example output:
# # defaultdict(<class 'list'>, {
# #   'UK': ['Liam', 'Noah'],
# #   'US': ['Ema', 'Olivia'],
# #   'China': ['Noah', 'Ema', 'Liam'],
# #   'Russia': ['Olivia']
# # })





# # 4---------------------------------------------
# # Counter — a dictionary subclass that counts hashable objects
# # Very useful for counting word frequencies, letters, etc.
# # ---------------------------------------------

# from collections import Counter  # Import Counter class from collections module

# file = 'test.txt'                # File to read text from
# f = open(file, 'r')              # Open the file in read mode
# data = f.read()                  # Read the entire content of the file into a string
# print(data)                      # Print the original text content

# # ------
# # Clean up punctuation marks to prepare for word counting


# cleanup = ' . , ! ? " '.split()  # List of punctuation marks to remove
# # cleanup = ['.', ',', '!', '?', '"', ''] (split() breaks by spaces)

# for mark in cleanup:             # Loop through each punctuation mark
#     data = data.replace(mark, '')  # Remove all instances of that mark from the text

# # ---------
# # Convert text to lowercase and split into words

# data = data.lower().split()      # Lowercase all text and split into words (by spaces)
# print(data[:10])                 # Show the first 10 words for preview

# # -------\
# # Count the frequency of each word

# counts = Counter(data)           # Create a Counter dictionary: {word: frequency}
# print(counts)                    # Print all word counts
# print(counts.most_common(10))    # Print the 10 most frequent words (word, count)





# --5-------------------------------------------
# Setting up a Character Index Application
# This program:
#   1. Reads a text file ('heart_dark.txt')
#   2. Splits the content into pages (paginate function)
#   3. Searches for specific words (characters) in the file (get_names function)
# ---------------------------------------------

from collections import defaultdict

# -------------------------------
# Function to create an index of names and their page numbers
# -------------------------------
def make_index(names, pages):
    # Create a dictionary where each key will be a name,
    # and the value will be a list of page numbers where that name appears
    index = defaultdict(list)
    
    # Convert names[0] to a list of individual names
    # Note: names seems to be a tuple, probably returned by get_names()
    names = list(names[0])  
    
    # Loop over each name to find which pages it appears on
    for name in names:
        # Pages are assumed to be a list of page content chunks
        # We loop over page numbers starting from 1
        for page in range(1, len(pages) + 1):
            # Check if the current name is in the current page
            if name in pages[page]:
                # If found, append the page number to the index for that name
                index[name].append(page)
    
    return index  # Return the completed index


# -------------------------------
# Function to print the index nicely
# -------------------------------
def print_index(index):
    # Loop over items in the index, sorted by name
    for name, pages in sorted(index.items()):
        # Print the name, left-aligned in a 20-character wide column
        print("{:20}".format(name), end="", flush=True)
        
        # Print all page numbers for that name
        # Separate with commas except for the last one
        for number in pages:
            print(number, end=", " if number != pages[-1] else " ")
        
        # Move to the next line after printing all pages
        print()


# ---------------------------------------------
# Example usage
# ---------------------------------------------

# Assume `data` is the text content of a document
pages = paginate(data, 30)  # Split data into pages of 30 lines/units
print(pages)                # Optional: show the page chunks

names = get_names(data)     # Extract names from the text
print(names)                # Shows tuple: (set of names, total matches)

# Create an index of names -> pages
index = make_index(names, pages)
print(index)                # Optional: see raw index dictionary
