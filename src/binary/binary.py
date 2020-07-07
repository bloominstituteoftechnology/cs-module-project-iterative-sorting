def find_value_binary(arr, value):
    
        
    first = 0
    last = (len(arr) - 1)
    #low is less than high
    while arr[first] <=  arr[last]:
        print('arr first', arr[first])
        mid = (first + last) // 2
        print('mid',arr[mid])
        print('first',arr[first])
        print('last',arr[last])
        if arr[mid] == value:
            return value
        elif arr[first] == value:
            return value
        elif arr[last] == value:
            return value
        # if value less than mid, make mid last
        elif arr[mid] < value:
            print('arr mid less')
            first = mid + 1
            last -= 1
        if value > make mid first
        elif arr[mid] > value:
            first = first + 1
            last = mid - 1
    return 'Not Found'

arr = [1,2,3,4,5,7,8,79,80]
print(find_value_binary(arr, 8))
            