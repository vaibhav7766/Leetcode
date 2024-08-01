#include <stdio.h>

int main() {
    printf("Mon\tTue\tWed\tThu\tFri\tSat\tSun\n");
    int space;
    printf("Enter number of spaces: ");
    scanf("%d", &space);

    int i = 1, j = 0;
    j += space;

    // Print initial tabs for the first week
    while (i <= space) {
        printf("\t");
        i++;
    }

    // Print the days of the month
    i = 1;
    while (i <= 31) {
        printf("%d\t", i);
        i++;
        j++;
        if (j == 7) {
            printf("\n");
            j = 0;
        }
    }
    return 0;
}
