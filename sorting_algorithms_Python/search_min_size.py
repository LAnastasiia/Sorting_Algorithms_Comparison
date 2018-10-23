import random
import copy
import time


def partition(arr, left, right):
    """
    Function for selecting the division point for the quick sort algorithm.
    :param arr:    array of numbers;
    :param left:   index of the left end of array;
    :param right:  index of the right end of array;
    :return:       index for a division point.
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


def quick_sort_ins(arr, left, right, min_size):
    """
    Function for the modification of Quick Sort algorithm with Insertion Sort on short sub arrays.
    :param arr:      array of numbers to sort;
    :param left:     index of the left end of array;
    :param right:    index of the right end of array;
    :param min_size  max arr_len for insertion sorting;
    :return:         sorted array (in ascending order).
    """
    if (right - left + 1 <= min_size) and (left < right):
        insertion_sort(arr, left, right)
    elif left < right:
        division_ind = partition(arr, left, right)    # choose a division point
        quick_sort_ins(arr, left, division_ind-1, min_size)
        quick_sort_ins(arr, division_ind+1, right, min_size)


def quick_sort(arr, left, right):
    """
    Function for the Quick Sort algorithm implementation.
    :param arr:      array of numbers to sort;
    :param left:     index of the left end of array;
    :param right:    index of the right end of array;
    :return:         sorted array (in ascending order).
    """
    if left < right:
        division_ind = partition(arr, left, right)
        quick_sort(arr, left, division_ind-1)
        quick_sort(arr, division_ind+1, right)


def insertion_sort(arr, left, right):
    for i in range(left, right+1):
        j = i
        while (j-1 >= 0) and arr[j] < arr[j-1]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr


def generate_random_array(arr_len):
    """
    Function for creating an array of pseudo-randomly chosen integers.
    :param arr_len: integer value of array's length;
    :return:        array of ints.
    """
    arr = [None] * arr_len
    for i in range(arr_len):
        arr[i] = random.randint(0, 10000000000)
    return arr


def count_average(lst):
    """
    Count average value of list's elements.
    :param lst: array;
    :return:    float value - average.
    """
    summ = 0
    for i in lst:
        summ += i
    return summ / len(lst)


def test_quick_sort_time(arr, left, right):
    a1 = copy.deepcopy(arr)
    # Count time.
    start = time.time()
    quick_sort(a1, left, right)
    finish = time.time()
    # Return time difference.
    return finish - start


def test_insertion_hybrid(arr, left, right, min_size):
    a1 = copy.deepcopy(a)
    # Count time.
    start = time.time()
    quick_sort_ins(a1, left, right, min_size)
    finish = time.time()
    # Return time difference.
    return finish - start


if __name__ =="__main__":
    # Set up initial values.
    MAX_LIM = 52                  # Maximum limit of min_size value.
    arr_len = 2 ** 10             # Starting length of tested arrays.
    max_arr_len = 2 ** 20         # Finish length for tested arrays.

    while arr_len <= max_arr_len:
        print('\n' + str(arr_len))

        good_sizes = []

        # Run 10 experiments.
        for i in range(5):
            a = generate_random_array(arr_len)
            # QUICK SORT.
            q_time = test_quick_sort_time(a, 0, arr_len-1)

            dict_min_size = dict((i, 0) for i in range(1, MAX_LIM+1))

            # Test all min_size values.
            for min_size in range(1, MAX_LIM+1):
                # INSERTION-QUICK SORT.
                i_time = test_insertion_hybrid(a, 0, arr_len-1, min_size)
                dict_min_size[min_size] = i_time

                # Fill in the dict.
                i_benefit = (q_time - i_time) / q_time * 100

                # Update best results.
                if i_benefit > 0:
                    dict_min_size[min_size] = i_benefit

            best_exp = max(dict_min_size, key=lambda x: dict_min_size[x])   # min_size, benefit
            good_sizes.append(best_exp)
            print(best_exp, dict_min_size[best_exp])

        # Output counted average value of min_size.
        res = round(count_average(good_sizes))
        print(arr_len, '-->', res)
        arr_len *= 2

