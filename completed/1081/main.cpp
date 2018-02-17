#define DEBUG_MODE

#ifdef DEBUG_MODE
#include <fstream>
#endif

#ifndef DEBUG_MODE
#define input_file cin
#endif

#include <cstdlib>
#include <iostream>
#include <string>

#define LL long long

using namespace std;

LL gcd(LL lhs, LL rhs)
{
    LL t = -1;
    if (lhs > rhs) swap(lhs, rhs);
    while (t != 0) {
        t = rhs % lhs;
        rhs = lhs;
        lhs = t;
    }
    return rhs < 0 ? -rhs : rhs;
}

void reduction(LL& lhs, LL& rhs)
{
    if (lhs != 0) {
        LL t = gcd(lhs, rhs);
        lhs = lhs / t;
        rhs = rhs / t;
    } else {
        lhs = 0;
        rhs = 1;
    }
}

void tongfen(LL& lhs, LL& rhs, LL& z, LL& w)
{
    lhs = (w * lhs) + (z * rhs);
    rhs = rhs * w;
}

void improper2proper(LL& lhs, LL& rhs)
{
    if (abs(lhs) > abs(rhs)) {
        lhs = lhs % rhs;
    }
}

int main()
{
    int test_case_num = 0;

#ifdef DEBUG_MODE
    ifstream input_file;
    input_file.open("input_file");
#endif
    while (input_file >> test_case_num) {
        char slash = '/';
        double total = 0;
        LL n = 0;
        LL d = 0;
        LL n_t = 0;
        LL d_t = 1;
        int times = 1;
        while (test_case_num--) {
            input_file >> n;
            input_file >> slash;
            input_file >> d;

            total = total + (double)n / d;
            tongfen(n_t, d_t, n, d);
            reduction(n_t, d_t);
            improper2proper(n_t, d_t);

            // cout<<"n: "<<n<<" d: "<<d<<endl;
            // cout<<"n_t: "<<n_t<<" d_total: "<<d_t<<endl;
        }

        // output
        if (total == 0) {
            cout << 0;
        } else if ((int)total == 0) {
            cout << n_t << "/" << d_t;
        } else {
            if (d_t == 1) {
                cout << (int)total;
            } else {
                cout << (int)total << " " << abs(n_t) << "/" << d_t;
            }
        }
        cout << endl;
    }
    return 0;
}
