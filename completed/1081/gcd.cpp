#include<iostream>
// #define NDEBUG
#include<cassert>
using namespace std;

long long gcd(long long x, long long y){
    long long t = -1;
    // sorting
    if(x > y){
        t = y; y = x; x = t;
    }
    // calculating gcd 
    while(t != 0){
        t = y % x;
        y = x;
        x = t;
    }
    return y;
}

int main(){
    assert(gcd(24, 60) == 12);
    assert(gcd(6, 30) == 6);
    assert(gcd(-3, 9) == -3);
    assert(gcd(3, 9) == 3);
}
