#include <stdio.h>
#include <time.h>
#include <stdint.h>
#include <stdlib.h>


void printArray(int arr[], int arr_len){
    for(int i = 0; i < arr_len; i++)
    {
        printf("%d  ", arr[i]);
    }
    printf("\n");
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
//
void slellSort(int arr[], int arr_len){
    for (int gap = arr_len / 2; gap > 0; gap /= 2) {
        for (int i= 0; i < arr_len-gap; i += gap){
            if (i - gap >= 0) & (arr[i-gap] > arr[i]){

                swapTwoValues(arr+i-gap, arr+i);
                i -= gap;
            }
        }
    }
}


int main() {
//    for (int arr_len = 65536; arr_len <= 262144; arr_len *= 2) {
        int arr_len = 524288;
        printf("%d: \n", arr_len);

        for (int l = 0; l < 10; l++) {
            int arr[arr_len];
            generateArray(arr, arr_len);

            clock_t start_time, end_time;
            double time_spent;
            start_time = clock();

            insertionSort(arr, arr_len);

            end_time = clock();
            time_spent = (double) (end_time - start_time) / CLOCKS_PER_SEC;
            printf("%f,  \n", time_spent);
        }
//        printf("\n\n");
//    }
}
