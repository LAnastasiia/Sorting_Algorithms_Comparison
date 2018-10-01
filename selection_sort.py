def selection_sort_list(arr):
    j = 0
    arr_len = len(arr)

    for j in range(arr_len):
        min_key, min_k_ind = arr[j], j

        for i in range(j, arr_len):
            if arr[i] < arr[j]:
                min_key, min_k_ind = arr[i], i

        arr[min_k_ind] = arr[j]
        arr[j] = min_key
    return arr


print(selection_sort_list([1, -45, 45, 22, 12]))
