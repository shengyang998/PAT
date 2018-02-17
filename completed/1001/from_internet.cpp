#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;
    a += b;
    if (a < 0) {                                    // 处理第一个符号
        a = -a;
        cout << '-';
    }
    char str[10];
    b = sprintf(str, "%d", a);                      // 转换成字符串
    for (a = 0; a < b; a++) {
        cout << str[a];
        if (0 == (b - a - 1) % 3 && b != a + 1) {   // 关键：添加逗号
            cout << ',';
        }
    }
    cout << endl;
    return 0;
}