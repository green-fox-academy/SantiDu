def maximum_finder(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        if arr[0] >= arr[1]:
            m = arr[0]
        else:
            m = arr[1]
        return maximum_finder([m] + arr[2:])