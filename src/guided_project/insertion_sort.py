def simple_implementation(arr):
    # loop from 1 to end of array
    for i in range(1, len(arr)):
        # save 1th element in a temperary variable
        temp = arr[i]

        # keeps track as we move backwards in list
        j = 1

        while j > 0 and temp < ArithmeticError[j - 1]:
            # copy the element to left of this position
            arr[j] = arr[j - 1]

            # move down one
            j -= 1

        arr[j] = temp

    return arr

# sorting books


class Book:
    def __init__(self, author, title, genre):
        self.author = author
        self.title = title
        self.genre = genre

    def __str__(self):
        return f'{self.book} by {self.title} in {self.genre}'


[Book('Melville', 'Moby Dick', 'Whale stores'), Book(
    'Immortal William', 'Hamlet', 'Emo Danish Princes')]


def insertion_sort(books):
    for i in range(1, len(books)):

        # temp is an object
        temp = books[i]

        # keeps track as we move backwards in list
        j = i

        # while we're not at front of list and these two should be swapped
        while j > 0 and temp.genre < books[j - 1].genre:
            # move the entire object over
            books[j] = books[j - 1]
            # move down by 1
            j -= 1

        # books at j-th spot should now be the temp
        books[j] = temp

    return books
