# Add up and print the sum of the all of the minimum elements of each inner array:
my_elems = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

# Grab indiv lists/tuples from my_elems
sum_this = []
for i in my_elems:
    # Grab the min for each indiv list/tuple
    elem_min = min(i)
    sum_this.append(elem_min)
    
print("Sum:", sum(sum_this))
# breakpoint()