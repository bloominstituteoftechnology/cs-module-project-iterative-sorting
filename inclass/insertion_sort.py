'''
Conceptualize a sorted half and an unsorted half 
Initially the sorted half consists of just the first element 
Iterate along the rest of the array 
Place it in its appropriate spot in the sorted half 
The sorted half grows until it encompasses the whole array 
'''

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

# def insertion_sort_books(arr_of_books):
#     # sort by the title 
#     for i in range(1, len(arr_of_books)):
#         curr_book = arr_of_books[i]
#         j = i
#         # put curr_book in the appropriate spot in our sorted half
#         # loop through our sorted half and find the appropriate spot 
#         while j > 0 and curr_book.title < arr_of_books[j - 1].title:
#             # taking the j - 1th book and copying it over to the jth spot 
#             # arr_of_books[j], arr_of_books[j - 1] = arr_of_books[j - 1], arr_of_books[j]
#             arr_of_books[j] = arr_of_books[j - 1]
#             j -= 1
#         # insert the book at the correct position 
#         arr_of_books[j] = curr_book

#     return arr_of_books

def insertion_sort_books(arr_of_books):
    for i in range(1, len(arr_of_books)):
        curr_book = arr_of_books[i]
        j = i

        while j > 0 and curr_book.title < arr_of_books[j - 1].title:
            arr_of_books[j], arr_of_books[j - 1] = arr_of_books[j - 1], arr_of_books[j]
            j -= 1

    return arr_of_books
 