def linear_search(arr, target):
    # Your code here
    arr_set = set(arr)
    print(arr_set)
    if target in arr_set:
        print("found")
    else:
        print("not found")
        return -1


#linear_search([-2, 7, 3, -9, 5, 1, 0, 4, -6], -9)

# Write an iterative implementation of Binary Search


def binary_search(arr, target):
    middle = arr[len(arr)//2]
    temp = []
    middle_value = arr[arr.index(middle)]
    print(arr, target, middle, arr.index(middle), middle_value)

    while len(arr) > 1:
        if target == middle_value:
            print("found: ", middle_value)
            return
        elif target < middle_value:
            temp = arr[:arr.index(middle)]
            arr = temp
            middle = arr[len(arr)//2]
            middle_value = arr[arr.index(middle)]
            print(arr)
        elif target > middle_value:
            temp = arr[arr.index(middle):]
            arr = temp
            middle = arr[len(arr)//2]
            middle_value = arr[arr.index(middle)]
            print(arr)
    """
    middle = arr[len(arr)//2]
    print(middle)
    if target == middle:
        print("found")
        return 1
    elif target < middle:
        arr = arr[]
        """
    return -1  # not found


#binary_search([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9], -6)
