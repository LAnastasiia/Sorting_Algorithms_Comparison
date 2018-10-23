def ins_partition(arr, left, right):
    pivot = arr[right]
    wall = left - 1
    current_ind = left

    while current_ind < right:
        if arr[current_ind] <= pivot:
            arr[current_ind], arr[wall+1] = arr[wall+1], arr[current_ind]
            wall += 1
        current_ind += 1
    arr[wall+1], arr[right] = arr[right], arr[wall+1]
    return wall+1


def ins_quick_sort(arr, left, right):
    """
    Function for the modification of Quick Sort algorithm with Insertion Sort on short sub arrays.
    """
    if (right - left + 1 <= 8) and (left < right):
        insertion_sort(arr, left, right)
    elif left < right:
        division_ind = ins_partition(arr, left, right)    # choose a division point
        ins_quick_sort(arr, left, division_ind-1)
        ins_quick_sort(arr, division_ind+1, right)


def partition(arr, left, right):
    """
    Function for selecting the division point for the quick sort algorithm.
    """
    pivot = arr[right]
    wall = left - 1
    current_ind = left

    while current_ind < right:
        if arr[current_ind] <= pivot:
            arr[current_ind], arr[wall+1] = arr[wall+1], arr[current_ind]
            wall += 1
        current_ind += 1
    arr[wall+1], arr[right] = arr[right], arr[wall+1]
    return wall+1


def quick_sort(arr, left, right):
    """
    Function for the Quick Sort algorithm implementation.
    """
    if left < right:
        division_ind = partition(arr, left, right)    # choose a division point
        quick_sort(arr, left, division_ind-1)
        quick_sort(arr, division_ind+1, right)


def insertion_sort(arr, left, right):
    for i in range(left, right+1):
        j = i
        while (j - 1 >= 0) and arr[j] < arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr


def _merge(arr_left, arr_right):
    """
    Merge together two parts of the list.
    """
    arr_res = []
    i, j = 0, 0
    while i < len(arr_left) and j < len(arr_right):
        if arr_left[i] <= arr_right[j]:
            arr_res.append(arr_left[i])
            i += 1
        elif arr_right[j] < arr_left[i]:
            arr_res.append(arr_right[j])
            j += 1
    # Complete sorted list with leftover elements of the longer sublist.
    if i < j:
        arr_res.extend(arr_left[i:])
    else:
        arr_res.extend(arr_right[j:])
    return arr_res


def merge_sort(arr):
    """
    Function for counting total number of inversions in the list using the Merge Sort algorithm.
    """
    if len(arr) <= 1:
        return arr
    else:
        half_ind = len(arr) // 2
        arr_left = merge_sort(arr[:half_ind])
        arr_right = merge_sort(arr[half_ind:])
        return _merge(arr_left, arr_right)


def m3_partition(arr, left, right):
    mid_ind = (right + left) // 2
    pivot_try = [arr[0], arr[mid_ind], arr[-1]]
    pivot = sorted(pivot_try)[1]

    arr[right], pivot = pivot, arr[right]
    pivot = arr[right]

    wall = left - 1
    current_ind = left

    while current_ind < right:
        if arr[current_ind] < pivot:
            arr[current_ind], arr[wall+1] = arr[wall+1], arr[current_ind]
            wall += 1
        current_ind += 1
    arr[wall+1], arr[right] = arr[right], arr[wall+1]
    return wall+1


def median_3_quick_sort(arr, left, right):
    if left < right:
        division_ind = m3_partition(arr, left, right)    # choose a division point
        median_3_quick_sort(arr, left, division_ind-1)
        median_3_quick_sort(arr, division_ind+1, right)


def m5_partition(arr, left, right):
    pivot_try = [left + ((right - left) * i // 4) for i in range(5)]
    pivot_try = sorted(pivot_try, key=lambda x: arr[x])
    pivot_ind = pivot_try[len(pivot_try) // 2]
    pivot = arr[pivot_ind]
    arr[right], arr[pivot_ind] = arr[pivot_ind], arr[right]

    wall = left - 1
    current_ind = left

    while current_ind < right:
        if arr[current_ind] <= pivot:
            arr[current_ind], arr[wall+1] = arr[wall+1], arr[current_ind]
            wall += 1
        current_ind += 1
    arr[wall+1], pivot = pivot, arr[wall+1]
    return wall+1


def median_5_quick_sort(arr, left, right):
    if left >= right:
        return arr
    else:
        division_ind = m5_partition(arr, left, right)    # choose a division point
        median_5_quick_sort(arr, left, division_ind-1)
        median_5_quick_sort(arr, division_ind+1, right)


def randomized_partition(arr, left, right):
    pivot_ind = random.randint(0, len(arr)-1)
    arr[pivot_ind], arr[right] = arr[right], arr[pivot_ind]
    pivot = arr[pivot_ind]
    wall = left - 1
    current_ind = left

    while current_ind < right:
        if arr[current_ind] <= pivot:
            arr[current_ind], arr[wall+1] = arr[wall+1], arr[current_ind]
            wall += 1
        current_ind += 1
    arr[wall+1], arr[right] = arr[right], arr[wall+1]
    return wall+1


def randomized_quick_sort(arr, left, right):
    if left < right:
        division_ind = randomized_partition(arr, left, right)    # choose a division point
        randomized_quick_sort(arr, left, division_ind-1)
        randomized_quick_sort(arr, division_ind+1, right)
