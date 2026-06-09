#include <stdio.h>
#include <time.h>

/* Constant Time: O(1) */
void constantTime() {
    int a = 10;
    int b = 20;
    int c = a + b;   // fixed number of operations
}

/* Linear Time: O(n) */
void linearTime(int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += i;
    }
}

/* Quadratic Time: O(n^2) */
void quadraticTime(int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            sum += i + j;
        }
    }
}

int main() {
    clock_t start, end;
    double time_taken;
    
    int sizes[] = {100, 500, 1000, 3000};
    int numSizes = sizeof(sizes) / sizeof(sizes[0]);

    for (int i = 0; i < numSizes; i++) {
        int n = sizes[i];
        printf("\nInput Size: %d\n", n);

        /* O(1) */
        start = clock();
        constantTime();
        end = clock();
        time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
        printf("O(1) Time: %f seconds\n", time_taken);

        /* O(n) */
        start = clock();
        linearTime(n);
        end = clock();
        time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
        printf("O(n) Time: %f seconds\n", time_taken);

        /* O(n^2) */
        start = clock();
        quadraticTime(n);
        end = clock();
        time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
        printf("O(n^2) Time: %f seconds\n", time_taken);
    }

    return 0;
}
