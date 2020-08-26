from itertools import compress
animals = ["Duck", "Jackal", "Hippo", "Cat", "Flammingo"]


def print_animalpairs():
    for animal1 in animals:
        for animal2 in animals:
            print(animal1, animal2)
            print(list(animal2))


print_animalpairs()
# res = list(zip(animals, animals[1:]+animals[:1]))

# print("The pair list is : " + str(res))
