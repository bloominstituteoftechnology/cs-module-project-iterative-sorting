# array with 1000 things in it
n = [None] * 1000

# O(1) - Not taking up anymore space. Just giving n back


def simple_function(n):
    return n


simple_function(n)

# O(n) - Space increases at the same rate as the size as our input increases


def make_another_array(n):
    inner_array = []

    for i in n:
        inner_array.append(i)

    return inner_array


make_another_array(n)

# O(n^2) - Doubled the input. Takes twice the amount of space


def make_matrix(n):
    matrix = []

    for item in n:
        row = []

        for i in n:
            row.append(i * 2)

        matrix.append(row)


def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)


factorial(3)
# 3 * 2 * 1 * 1
