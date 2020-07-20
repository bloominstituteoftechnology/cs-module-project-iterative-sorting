"""
O(n) - Linear Time
"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']


def print_animals(animal_list):
    for i in range(len(animal_list)):
        print(animal_list[i])


"""
What about this one? What runtime complexity is this one?
"""


def print_animals(animal_list):  # O(n * (1 + 1 + 1 * (1)) = O(n + 3) = O(n)
    for i in range(len(animal_list)):  # O(n + 1 + 1 + 1 * (1)) = O(n + 3) = O(n)
        print(animal_list[i])  # O(1)
        my_number = 0  # O(1)
        for _ in range(100000):  # O(1)
            my_number += 1  # O(1)


"""
CFU: Slack Thread: Why doesn't the nested for loop make the time complexity O(n^2)?
"""

"""
O(n^2) & O(n^3) - Polynomial Time
"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']

# Print a list of all possible animal pairs


def print_animal_pairs(animal_list):  # O(n^2)
    for animal_1 in animal_list:  # O(n)
        for animal_2 in animal_list:  # O(n)
            print(f"{animal_1} - {animal_2}")


# Print a list of all possible animal triples


def print_animal_triples():  # O(n^3)
    for animal_1 in animals:
        for animal_2 in animals:
            for animal_3 in animals:
                print(f"{animal_1} - {animal_2} - {animal_3}")


# Print a list of all possible animal triples


def print_animal_triples():  # O(n^3)
    for animal in animals:  # O(n)
        print(animal)


for animal_1 in animals:  # O(n^3)
    for animal_2 in animals:
        for animal_3 in animals:
            print(f"{animal_1} - {animal_2} - {animal_3}")


# Example
x = 0
while x < n * n * n:
    x = x + (n * n)


"""
CFU: Slack Thread
What's the time complexity to print all animal quintuples? What about "ten" tuples?
"""

"""
O(log n) - Logarithmic Time
"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']

# free all the animals, half at a time
# (remove them from the array)


def free_animals(animal_list):
    while len(animal_list) > 0:
        animal_list = animal_list[0: len(animal_list) // 2]


# We are reducing by half at each step
# This is the inverse of doubling at each step O(2^n) - Exponential Time

# Step 0: 100000
# Step 1: 50000
# Step 2: 25000
# Step 3: 12500
# Step 4: 6250
# Step 5: 3125
...
# Step 17: 1​

# Example 2
sum = 0
n = 10
for i in range(n):  # O(n * (1 + (log n))) = O(n * log n) = O(n log n)
    j = 1  # O(1)
    while j < n:  # O(log n)
        j *= 2
        sum += 1

"""
CFU: Slack Thread
What's the worst the number of steps can get for a O(log n) time complexity
algorithm with an input size of 10 million?
"""
