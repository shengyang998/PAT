// 畅通工程
// 并查集
#include<cstdio>
using namespace std;

#define N 1001
int Tree[N];

int findRoot(int x){
  int res;
  int tmp = x;
  while(Tree[x] != -1){
    x = Tree[x];
  }
  res = x;
  x = tmp;
  int t;
  while(Tree[x] != -1){
    t = Tree[x];
    Tree[x] = res;
    x = t;
  }
  return res;
}

int main(){
  int n, m;
  int road[1001][2];
  for (int i=0; i<1001; i++){
    road[i][0] = -1;
    road[i][1] = -1;
  }
  while(scanf("%d", &n)!=EOF && n != 0){
    scanf("%d", &m);
    for(int i=1; i<=n; i++)
      Tree[i] = -1;
    while(m-- != 0){
      int a, b;
      scanf("%d %d", &a, &b);
      a = findRoot(a);
      b = findRoot(b);
      if(a!=b) Tree[a] = b;
    }
    int ans = 0;
    for(int i=1; i<=n; i++){
      if(Tree[i] == -1)
        ans++;
    }
    print("%d\n", ans-1)
  }
  return 0;
}
