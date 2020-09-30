# O(n log n + log n) --> what is dominant term? -> 
# O(n log n)
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear', 'Goose']

animals.sort()  # O(n log n)
print(animals)

def binary_search(a): #(log n)
    pass

print(binary_search('Fish'))

# Linear search, O(n) over number of animals
def find_animal(a):
    for animal in animals: # O(n) over number of animals
        if animal == a:
            return True
    return False

print(find_animal('Goose'))
print(find_animal("Rockfish"))