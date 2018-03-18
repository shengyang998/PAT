#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
  // input
  int n, m, k;
  scanf("%d %d %d", &n, &m, &k);
  // get the graph
  int c1, c2;
  for(int i=0; i<m; i++){
    scanf("%d %d", &c1, &c2);
    roads[c1][c2] = 1;
  }
  int de_city;
  for(int i=0; i<k; i++){
    scanf("%d", &de_city);
    int pool[100];
    for (int j = 0; j < n + 1; j++) {
        for (int g = 0; g < n + 1; g++) {
            roads[j][g];
        }
    }
  }
  return 0;
}
