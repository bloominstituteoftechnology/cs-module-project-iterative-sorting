def find_value_binary(arr, value):
    first = 0
    last = (len(arr) - 1)

    found = False

    while first <= last and not found:
        #find middle using integer division
        middle = (last - first)//2

        if arr[middle] == value
            