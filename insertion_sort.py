 
my_list = [8, 2, 5, 4, 1, 3, 7, 6]

def insertion_sort_not_in_place(unsorted_list):
    sorted_list = []

    for n in unsorted_list:
        # if len(sorted_list) == 0:
        #     sorted_list.append(n)
        #     continue
        index = 0
        for i in range(len(sorted_list) - 1, -1, -1):
            if sorted_list[i] < n:
                index = i +1
                break
        sorted_list.insert(index, n)


    return sorted_list


sorted_list = insertion_sort_not_in_place(my_list)
print(sorted_list)

def insertion_sort(a):
    for i in range(1, len(a)):
        val = a[i]
        
        j = i
        while j > 0 and val < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j] # swap
            j -= 1
        

print(insertion_sort(my_list))
print(my_list)