# This module contains an insertion sort function for a python list.


def insertion_sort_list(arr):
    """
    (list) --> (list)
    This function performs an insertion sort algorithm on a python list.
    """
    arr_len = len(arr)  # save the length to avoid recounting it in the loop

    for j in range(1, arr_len):
        mov_key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > mov_key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = mov_key

    return arr


example_arr = [23, 12, 0, 45, 45, 44, 12, 1]
example_arr = [-1, 1, -2]
print(insertion_sort_list(example_arr))
