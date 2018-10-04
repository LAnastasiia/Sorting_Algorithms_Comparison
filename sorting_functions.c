#include <stdio.h>
#include <time.h>
#include <stdint.h>
#include <stdlib.h>


void printArray(double arr[], int arr_len){
    for(int i = 0; i < arr_len; i++)
    {
        printf("%f, ", arr[i]);
    }
    printf("\n");
}

void copyArray(int arr[], int copy_arr[], int arr_len){
    for (int i = 0; i < arr_len; i++) {
        copy_arr[i] = arr[i];
    }
}


void generateArray(int arr[], int arr_len){
    for(int n = 0; n < arr_len; n++){
        arr[n] = rand();
    }
}


void swapTwoValues(int *ind1, int *ind2) {
    int temp_key = *ind1;
    *ind1 = *ind2;
    *ind2 = temp_key;
}


void selectionSort(int arr[], int arr_len){
    for(int i = 0; i <= arr_len-1; i++)
    {
        int min_key_ind = i;
        for(int j=i; j < arr_len; j++)
        {
            if (arr[j] < arr[min_key_ind]){
                min_key_ind = j;
            }
        }
        swapTwoValues(arr + min_key_ind, arr + i);
    }
}


void insertionSort(int arr[], int arr_len){
    for(int i = 1; i <= arr_len-1; i++)
    {
        for(int j=i; j > 0; j--)
        {
            if (arr[j-1] > arr[j]) {
                swapTwoValues(arr + j - 1, arr + j);
            }
        }
    }
}


void shellSort(int arr[], int arr_len){
    for (int gap = arr_len / 2; gap > 0; gap /= 2)
    {
        for (int i = 0; i < arr_len - gap; i += gap)
        {
            int j = i + gap;
            while ((j - gap >= 0) && (arr[j] < arr[j - gap])){
                swapTwoValues(arr+j, arr+j-gap);
                j = j - gap;
            }
        }
    }
}


int main() {
    for(int arr_len = 16384; arr_len <= 262144; arr_len *=2) {
//        int  arr_len = 2048;                                                    // length of arr
        int arr[arr_len];                                                         // initialize original array
        double insertion_results[10], selection_results[10], shell_results[10];   // initialize results arrays

        // run for 5 different arrays
        int l;
        for (int l = 0; l < 10; l++) {
            generateArray(arr, arr_len);                                          // make content in arr
            clock_t start_time, end_time;                                         // initialize timers
            double time_spent;                                                    // initialize result time var
            int shell_copy[arr_len], ins_copy[arr_len], sel_copy[arr_len];        // init copies of arr



            copyArray(arr, shell_copy, arr_len);                  // copy arr for SHELL
            start_time = clock();
            shellSort(shell_copy, arr_len);
            end_time = clock();
            time_spent = (double) (end_time - start_time) / CLOCKS_PER_SEC;
            shell_results[l] = time_spent;




            copyArray(arr, ins_copy, arr_len);                  // copy arr for INSERTION
            start_time = clock();
            insertionSort(ins_copy, arr_len);
            end_time = clock();
            time_spent = (double) (end_time - start_time) / CLOCKS_PER_SEC;
            insertion_results[l] = time_spent;




            copyArray(arr, sel_copy, arr_len);                  // copy arr for INSERTION
            start_time = clock();
            selectionSort(sel_copy, arr_len);
            end_time = clock();
            time_spent = (double) (end_time - start_time) / CLOCKS_PER_SEC;
            selection_results[l] = time_spent;

        }
        // RESULTS
        printf("INSERTION: ");
        printArray(insertion_results, 10);
        printf("SELECTION: ");
        printArray(selection_results, 10);
        printf("SHELL:     ");
        printArray(shell_results, 10);
        printf("\n\n");
    }
}
