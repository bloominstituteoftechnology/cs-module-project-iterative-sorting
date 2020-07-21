import random
import time  # We'll use this later

my_range = 100
my_size = 10

my_random = random.sample(range(my_range), my_size)
print(my_random)

searching_for = 7


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True

    return False


print(linear_search(my_random, searching_for))


"""
CFU: Slack Thread
What's the runtime complexity of a linear search?
"""




def find_value_binary(arr, value):
    first = 0
    last = (len(arr) - 1)

    found = False

    while first <= last and not found:
        # find middle using integer divsion
        middle = (first + last) // 2

        if arr[middle] == value:
            found = True

        else:
            if value < arr[middle]:
                # search lower half of remainder
                last = middle - 1
            else:
                # search upper half of remainder
                first = middle + 1

    return found


# Sort the array of numbers
my_random.sort()
print(find_value_binary(my_random, searching_for))


"""
CFU: Slack Thread
What's the runtime complexity of a binary search?
"""

# """
# The First Test
# """

# print("Linear")
# start = time.time()
# print(linear_search(my_random, searching_for))
# end = time.time()
# print(f"Runtime: {end - start}")

# print("Binary")
# start = time.time()
# my_random.sort()
# print(find_value_binary(my_random, searching_for))
# end = time.time()
# print(f"Runtime: {end - start}")


"""
The Second Test
"""

print("Linear")
start = time.time()
print(linear_search(my_random, searching_for))
end = time.time()
print(f"Runtime: {end - start}")

print("Linear Again")
start = time.time()
print(linear_search(my_random, searching_for))
end = time.time()
print(f"Runtime: {end - start}")

print("Binary")
start = time.time()
my_random.sort()
print(find_value_binary(my_random, searching_for))
end = time.time()
print(f"Runtime: {end - start}")

print("Binary _after_ sort")
start = time.time()
print(find_value_binary(my_random, searching_for))
end = time.time()
print(f"Runtime: {end - start}")


"""
CFU: Slack Thread
When is binary search better? When is linear search better?
"""



# Example 3
"""
Suppose that you have an n-rung ladder and plenty of toy cars.

Suppose also that a toy car gets broken if it is thrown off rung r or higher,
and doesn't get broken if dropped off a runn less than floor r.

Devise a strategy to determine the value of r
such that the number of dropped + broken toy cars is minimized.
"""