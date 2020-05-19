'''
Determining time complexity:

1. Compute the big O of each line in isolation.
2. If something is in a loop, multiply its big O by the number of iterations of the loop
3. If two things happen sequentially, add the big Os.
4. Drop leading multiplicative constants from each big O.
5. From all the Big-Os that are added, drop all but the biggest, dominating one.
'''




'''
Space (or memory) complexity measures how much _additional_ memory an 
algorithm allocates in order to run.

One big giveaway that an algorithm is utilizing additional memory is 
if it initializes a data structure. 

We use the same big O notation when talking about space complexity.

Just like with time complexity, space complexity is concerned with the worst case. 
'''

# O(n) time, O(1) space 
def o_1_space(n):
    total = 0  # O(1)

    # range returns a `range` 
    # does the range object utilize a constant amount of space?
    # range takes up a constant amount of space 
    for i in range(n): # O(1) space 
        total += i  # O(1)

    return total 


# O(n) time, O(n) space 
def o_n_space(n):
    sums = []

    for i in range(n):
        sums.append(i + i)  # O(n)

    return sums


# O(n^2) time, O(n^2) space
def o_n2_space(n):
    times_table = []

    for i in range(n):  # O(n) time 
        row = []

        for j in range(n):  # O(n) time
            row.append(j * i)  # we're adding n elements to the `row` list; O(n) space 

        times_table.append(row)  # we have n lists that each hold n elements 

    return times_table  # O(n^2)



# O(n^2) space
def o_2_space_v2(n):
    times_table = []

    for i in range(n):
        times_table.append(i)

        for j in range(n):
            times_table.append(j)

    return times_table



# space complexity cares about how much _additional_ space is being used 
# O(1) space 
# don't count data structures that are passed in as input 
def foo(arr):
    for x in arr:
        print(x + x)



# O(n) space 
def bar(arr):
    output = []

    for n in arr:
        output.append(n * n)  # O(n) space 

    return output


# arr is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# O(n)
def baz(arr):
    evens = []

    # we're adding half of the values from the input array 
    for n in arr:
        if n % 2 == 0:
            evens.append(n) # O(n / 2) == O(1/2 * n) ~ O(n) space 

    return evens



# Pass by reference: the function is receiving a pointer to the input 
# Pass by value: the function is receiving a copy of the input O(n)