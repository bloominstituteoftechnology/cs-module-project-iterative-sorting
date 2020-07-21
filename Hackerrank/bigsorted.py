def bigSorting(unsorted):
    # arr = []
    # for x in unsorted:
    #     arr.append(int(x))
    # result = sorted(arr) 
    # return result
    unsorted.sort(key=int)
    for s in unsorted:
        print(s)
    return unsorted

        
    #     print('i', i)
    #     current = i
    #     previous = i - 1
    #     print('current', current)
    #     print(int(unsorted[current]), int(unsorted[previous]), i  )
    #     while int(unsorted[current]) < int(unsorted[previous]) and previous >= 0:
    #         unsorted[current], unsorted[previous] = unsorted[previous], unsorted[current]
    #         current -= 1
    #         previous -= 1
    #         print(unsorted)
            
    # return unsorted
unsorted = ['6', '3142220', '1', '3', '10', '3', '5']
print(bigSorting(unsorted))


# def bigSorting(unsorted):
    
#     for i in range(1, len(unsorted)):
#         print('i', i)
#         current = i
#         previous = i - 1
#         print('current', current)
#         print(int(unsorted[current]), int(unsorted[previous]), i  )
#         while int(unsorted[current]) < int(unsorted[previous]) and previous >= 0:
#             unsorted[current], unsorted[previous] = unsorted[previous], unsorted[current]
#             current -= 1
#             previous -= 1
#             print(unsorted)
            
#     return unsorted
# unsorted = ['6', '3142220', '1', '3', '10', '3', '5']
# print(bigSorting(unsorted))