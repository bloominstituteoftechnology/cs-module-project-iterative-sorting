import random
import time
my_range = 10000000
my_size = 150000

# nums = list(range(0, my_size))
# shuffled_nums = list(range(0, my_size))
# random.shuffle(shuffled_nums)

random_nums = random.sample(range(my_range), my_size)
# random_nums = [79, 48, 73, 77, 38, 68, 45, 24, 75, 62, 59, 4, 33, 49, 54]


# print(nums)
# print(random_nums)
# print(shuffled_nums)


num_to_find = 12

# o(n)


def linear_search(arr, target):
    for num in arr:
        if num == target:
            # print("its in position", arr[num])
            return True
    return False


print("Linear")
start = time.time()
print(linear_search(random_nums, num_to_find))
end = time.time()
print(f"Runtime: {end-start}")

# print(linear_search(shuffled_nums, num_to_find))
# print(linear_search(nums, num_to_find))
random_nums.sort()
# print(random_nums)


def binary_search(arr, target):
    # * find middle point (index)    = (start + end)/2
    # * compare the value in the middle with target
    # * shrinking and modifying arays are not very efficient

    # ? [79, 48, 73, 77, 38, 68, 45, 24, 75, 62, 59, 4, 33, 49, 54]
    # ?  ^                        ^
    # ?  start                    end/2

    # ? [79, 48, 73, 77, 38, 68, 45]
    # ?  ^            ^
    # ?  start      end/2
    start = 0
    end = (len(arr)-1)

    found = False
    while end >= start and not found:
        middle_index = (start + end)//2
        # * compare the value in the middle with the target
        # * check  if middle val is the same as target, set found to True
        if arr[middle_index] == target:
            found = True
        # * move start or end index closer to one another, and shrink our search space
        else:
            if target < arr[middle_index]:
                # * search left hand side
                # * move pointers
                # * end is median - 1 :  the middle is not even your target anyway
                end = middle_index - 1
            if target > arr[middle_index]:
                start = middle_index + 1

    return found


random_nums.sort()

print("Binary")
start = time.time()
print(binary_search(random_nums, num_to_find))
end = time.time()
print(f"Runtime: {end-start}")


# print(binary_search(random_nums, 9))
