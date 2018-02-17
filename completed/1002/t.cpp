#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int main()
{
    vector<int> a1{1,2,3,4,5,6,7,8};
    a1.reserve(20);
    if(find(a1.begin(), a1.end(), 8) != a1.end()){
        cout << "yes" << endl;
    }

}
