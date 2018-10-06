#include <time.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>


struct LongInt {
    int*   length;
    int*  numbers_arr;
} comp_count;


void addToLongInt(struct LongInt number, int i){
    if (number.numbers_arr[i] < 9) {
        number.numbers_arr[i]++;
    }
    else {
        number.numbers_arr[i] = 0;             // 89 --> 90

        if (i >= (number.length[0]-1))         // 99+1
        {
            number.length[0]++;
        }

        if (number.numbers_arr[i+1] == 9){    // 5499
            return addToLongInt(number, i+1);
        }
        else {
            number.numbers_arr[i + 1]++;
        }
    }
}

void freeLongInt(struct LongInt number){
    for (int i =0; i < number.length[0]; i++){
        number.numbers_arr[i] = 0;
    }
    number.length[0] = 1;
}


void printArray(double arr[], int arr_len){
    for(int i = 0; i < arr_len; i++)
    {
        printf("%f, ", arr[i]);
    }
    printf("\n");
}


void printLongIntArray(int arr[], int arr_len[]){
//    printf("%d\n", arr_len[1]);
    int len = arr_len[0];
    for(int i = len-1; i >= 0; i--)
    {
        printf("%d", arr[i]);
    }
}

void generateBackOrdArray(int arr[], int arr_len){
    for(int i = arr_len; i > 0; i--){
        arr[i] = i;
    }
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


void generateOrdArray(int arr[], int arr_len){
    for(int i =0; i < arr_len; i ++){
        arr[i] = i;
    }
}

void swapTwoValues(int *ind1, int *ind2) {
    int temp_key = *ind1;
    *ind1 = *ind2;
    *ind2 = temp_key;
}


double selectionSort(int arr[], int arr_len){
    int* long_len = (int*) malloc(2 * sizeof(int));
    int* long_num = (int*) malloc(1000000000 * sizeof(int));
    struct  LongInt comp_count;
    comp_count.numbers_arr = long_num;
    comp_count.length = long_len;

    clock_t start_time, end_time;
    double time_spent;

    start_time = clock();
    for(int i = 0; i <= arr_len-1; i++)
    {
        int min_key_ind = i;
        for(int j=i; j < arr_len; j++)
        {
            if (arr[j] < arr[min_key_ind]){

                min_key_ind = j;
            }
            addToLongInt(comp_count, 0);
        }
        addToLongInt(comp_count, 0);     // +1 comparison by the end of loop
        swapTwoValues(arr + min_key_ind, arr + i);
    }
    end_time = clock();
    time_spent = (double) (end_time - start_time) / CLOCKS_PER_SEC;
    printf("SELECTION: ");
    printLongIntArray(comp_count.numbers_arr, comp_count.length);
    freeLongInt(comp_count);
    return time_spent;
}


double insertionSort(int arr[], int arr_len){
    int* long_len = (int*) malloc(2 * sizeof(int));
    int* long_num = (int*) malloc(1000000000 * sizeof(int));
    struct  LongInt comp_count;
    comp_count.numbers_arr = long_num;
    comp_count.length = long_len;

    clock_t start_time, end_time;
    double time_spent;

    start_time = clock();
    for(int i = 1; i < arr_len; i++)
    {
        int j = i;
        while (j > 0 && arr[j-1] > arr[j])
        {
            swapTwoValues(arr+j, arr+j-1);
            j--;
            addToLongInt(comp_count, 0);
        }
        addToLongInt(comp_count, 0);     // + 1 comparison when arr[j] < mov_key
    }
    end_time = clock();
    time_spent = (double) (end_time - start_time) / CLOCKS_PER_SEC;
    printf("INSERTION: ");
    printLongIntArray(comp_count.numbers_arr, comp_count.length);
    freeLongInt(comp_count);
    return time_spent;
}


double shellSort(int arr[], int arr_len){
    int* long_len = (int*) malloc(2 * sizeof(int));
    int* long_num = (int*) malloc(1000000000 * sizeof(int));
    struct  LongInt comp_count;
    comp_count.numbers_arr = long_num;
    comp_count.length = long_len;

    clock_t start_time, end_time;
    double time_spent;

    start_time = clock();
    for (int gap = arr_len / 2; gap > 0; gap /= 2)
    {
        for (int i = 0; i < arr_len; i += gap)
        {
            int j = i;
            while (j - gap >= 0 && arr[j] < arr[j - gap]){
                swapTwoValues(arr+j, arr+j-gap);
                j = j - gap;
                addToLongInt(comp_count, 0);
            }
            addToLongInt(comp_count, 0);   // +1 comparison after while-loop condition turning False
        }
    }
    end_time = clock();
    time_spent = (double) (end_time - start_time) / CLOCKS_PER_SEC;
    printf("SHELL:     ");
    printLongIntArray(comp_count.numbers_arr, comp_count.length);
    freeLongInt(comp_count);
    return time_spent;
}



int main() {

    for(int arr_len = 2048; arr_len <= 131072; arr_len *= 2){
        int *arr = (int *) malloc(arr_len * sizeof(int));
        int se_copy[arr_len], in_copy[arr_len], sh_copy[arr_len];

        printf("%d\n", arr_len);

        for(int i = 0; i < 10; i++){
            generateArray(arr, arr_len);
            copyArray(arr, se_copy, arr_len);
            copyArray(arr, in_copy, arr_len);
            copyArray(arr, sh_copy, arr_len);

            printf("           %f\n", selectionSort(se_copy, arr_len));
            printf("           %f\n", insertionSort(in_copy, arr_len));
            printf("           %f\n", shellSort(sh_copy, arr_len));
        }
        printf("\n\n");
    }
}
