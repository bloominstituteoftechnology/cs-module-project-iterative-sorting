a = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]

for x in a:
    if x % 3 == 0:
        print(x)

# Print out all of the strings in the following array that represent a number divisible by 3

b = [
    "five",
    "twenty six",
    "nine hundred ninety nine",
    "twelve",
    "eighteen",
    "one hundred one",
    "fifty two",
    "forty one",
    "seventy seven",
    "six",
    "twelve",
    "four",
    "sixteen"
]

# expected output:
# nine hundred ninety nine
# twelve
# eighteen
# six
# twelve

c = {
    "five": 5,
    "twenty six": 26,
    "nine hundred ninety nine": 999,
    "twelve": 12,
    "eighteen": "18",
    "one hundred one": 101,
    "fifty two": 52,
    "forty one": 41,
    "seventy seven": 77,
    "six": 6,
    "twelve": 12,
    "four": 4,
    "sixteen": 16
}

for key, value in c.items():
    if int(value) % 3 == 0:
        print(key)
