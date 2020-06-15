py_list = ['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]

# for item in py_list:
#     print(item)

[print(f"{n} is a numbers in the list") for n in py_list if type(n) == int or type(n) == float or n.isdigit()]
