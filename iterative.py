animals = ['Duck', 'Jacka', 'Aar', 'cat', 'cat']

# Print all the animals
# How much longer is this going to take to run as the size of the data set increase?
# If we double it, twice as long
# If we ahlve it, half as long
# If we triple it, three times as long
# Linear time, O(n)


def print_animals():
    for a in animals:  # O(n) over the number of animals
        print(a)


def print_animal(i): # O(1) over the number of animas
    print(animals[i])

def print_animal_2(i):  # O(1) over the number of animals
    for c in animals[i]:   # O(1) over the number of animas
        print(c)


'''
1. wrirte down the big O of each line in isloation
2. loop get O(n)
3. most other single lines get O(1)
4. Add the big Oof the thing sin series
5. Multiply the big O of each loop by its body
'''

def find_dups():
    for i0 in range(len(animals)): # n (over number of animals) --> O(n*n) -> O(n^2)
        for i1 in range(len(animals)): # n (over number of animals) --> with loop mulitply O(n*1) -> O(n)
            if i0 == i1:                # 1  O(1) --> adds up to 4 but drop 4 as it is constant 
                continue                
            if animals[i0] == animals[i1]: 
                print(f"duplicate: {animals[i0]} ")

find_dups()


def print_animals_3():
    # O(n+2) == O(2n) --> O(n) --> add if they in sequence, multiply if loop
    for a in animals:  # O(n) 
        print(a)

    for a in animals:  # O(n) 
        print(a)

for i in range(100000000000000000): # O(1)
    print(animals[0]) # O(1)

for i in range(10): # O(1)
    print(animals[0]) # O(1)

'''
Beeter than O(n):
    O(log n)
    o(1)

Worse, but not bad:
    O(n log n)
Bad:
    O(n^2)
    O(n^3)
    O(2^n)
    O(n!)
'''