// A+B Format
// Ysy 2017-08-04

#include <cstring>
#include <fstream>
#include <iostream>

#define DEBUG

#define LL long long

#ifndef DEBUG
#define input cin
#endif

using namespace std;

int main()
{
#ifdef DEBUG
    ifstream input("input_file");
#endif
    LL a = 0;
    LL b = 0;
    char temp[30]; // -9991
    char res[30]; // 199,9-
    char reverse_res[30]; // -9,991
    int len = 0;
    input >> a >> b;
    sprintf(temp, "%lld", a + b);

    for (int i = strlen(temp), j = 1; i > 0; i--, j++) {
        if (temp[i - 1] == '-' && len != 0 && res[len - 1] == ',') {
            res[len - 1] = temp[i - 1];
        } else {
            res[len++] = temp[i - 1];
        }
        if (j % 3 == 0 && i != 1) {
            res[len++] = ',';
        }
    }
    len = 0;

    for (int i = strlen(res); i > 0; i--) {
        reverse_res[len++] = res[i - 1];
    }
    cout << reverse_res;

    return 0;
}