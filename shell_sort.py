def shell_sort_arr(arr):
    """
    (list) --> (list)
    This function performs the Shell Sort algorithm on a Python list.
    """
    arr_len = len(arr)       # Secure the length value to avoid recounting.
    gap = arr_len // 2       # Establish the first value of gap.

    while gap > 0:
        for i in range(arr_len - gap):
            print(arr[i], '-', arr[i+gap])
            j = i + gap
            while (j - gap >= 0) and (arr[j] < arr[j - gap]):
                mov_el = arr[j]        # Secure the value of moving element.
                arr[j] = arr[j-gap]    # Swap wrongly ordered values.
                arr[j-gap] = mov_el
                j -= gap
        gap = gap // 2                 # Decrease the gap.

    return arr

print(shell_sort_arr([2, -8, 9, 5, 6, 1, 18, 11]))
