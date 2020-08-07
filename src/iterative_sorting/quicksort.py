
# [5,9,3,7,2,8,1,5]

# pivot = 5

# [3,2,1][5][9,7,8,6]

def partion(numbers):
    # break list into left subarray, pivot and right subarray
    
    right = []
    
    for num in numbers[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)
    return left, pivot, right

def quicksort(numbers):
    if numbers == []:
        return numbers
    left, pivot, right = partion(numbers)  
    return quicksort(left) + [pivot] + quicksort(right)
