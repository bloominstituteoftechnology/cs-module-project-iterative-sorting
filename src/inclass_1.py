animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat', 'Flamingo',
            'Giraffe', 'Elephant', 'Bear', 'Dog', 'Goose', 'Antelope']


# implement bin search
def find_animal(a):
    for animal in animals:
        if animal == a:
            return True

    return False


print(find_animal('Goose'))
print(find_animal('Rockfish'))
