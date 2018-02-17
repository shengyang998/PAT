// 1003 Emergency with cpp
// from internet

#include<cstdio>
#include<algorithm>

using namespace std;

int n, m, c1, c2;
int e[510][510]; // edges
int weight[510]; // weight
int dist[510];   // min dist
int num[510];    // points' shortest path number
int w[510];      // points' weight
bool visit[510];
const int inf = 99999999;

int main(){
  scanf("%d%d%d%d", &n, &m, &c1, &c2);
  for (int i=0; i<n; i++){
    scanf("%d", &weight[i]);
  }
  fill(e[0], e[0]+510*510, inf);
  fill(dist, dist+510, inf);
  int a, b, c; // get the graph
  for(int i=0; i<m; i++){
    scanf("%d%d%d", &a, &b, &c);
    e[a][b] = c;
    e[b][a] = c;
  }
  // init for dijkstra
  dist[c1] = 0;
  w[c1] = weight[c1];
  num[c1] = 1;
  for(int i=0; i<n; i++){
    int u = -1, minn = inf;
    for(int j = 0; j<n; j++){
      if(visit[j] == false && dist[j]<minn){
        u = j;
        minn = dist[j];
      }
    }
    if(u == -1) break;
    visit[u] = true;
    for(int v = 0; v<n; v++){
      if(visit[v] == false && e[u][v] != inf){
        if(dist[u] + e[u][v] < dist[v]){
          dist[v] = dist[u] + e[u][v];
          num[v] = num[u];
          w[v] = w[u] + weight[v];
        }
        else if(dist[u] + e[u][v] == dist[v]){
          num[v] = num[v] + num[u];
          if(w[u] + weight[v] > w[v]){
            w[v] = w[u] + weight[v];
          }
        }
      }
    }
  }
  printf("%d %d\n", num[c2], w[c2]);
  return 0;
}
