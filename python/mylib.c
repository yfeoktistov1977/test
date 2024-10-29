#include <stdio.h>

typedef struct {
    int id;
    double value;
    char name[50];
} Data;


// Function to add two integers
int add(int a, int b, char *str) {
    printf("\n !!!!! From lib !!!! a=%d b=%d str=%s \n", a ,b, str);
    return a + b;
}

void print_data(const Data* data) {
    printf("ID: %d\n", data->id);
    printf("Value: %.2f\n", data->value);
    printf("Name: %s\n", data->name);
}
