animals = ['Duck', 'Jackal', 'Hippo', 'Cat', 'Aardvark', 'Cat', 'Flamingo', 
            'Iguana', 'Giraffe', 'Elephant', 'Bear']
for a in animals:
    print(a)

def print_animal(i):
    print(animals[i])

def print_animal_2(i):
    for c in animals[i]:
        print(c)
print_animal_2(3)

def find_dups():
    for i0 in range (len(animals)):
        if [i0] == [i1]:
            continue
        if animals[i0]== animals[i1]:
            print(f"Duplicate: {animals[i0]}")

find_dups()