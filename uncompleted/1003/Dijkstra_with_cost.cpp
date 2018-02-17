// Dijkstra with point cost from Wangdao
//

#include<cstdio>
#include<vector>
using namespace std;
struct E{
  int next;
  int c;
  int cost;
};
vector<E> edge[1001];
int dist[1001];
int cost[1001];
bool mark[1001];
int main(){
  int n, m;
  int S, T; // source, target

  // get graph and source, target
  while(scanf("%d%d", &n, &m)!=EOF){
    if(n==0 && m==0) break;
    for (int i=1; i<=n; i++) edge[i].clear();
    while(m--){
      int a, b, c, cost;
      scanf("%d%d%d%d", &a, &b, &c, &cost);
      E tmp;
      tmp.c = c;
      tmp.cost = cost;
      tmp.next = b;
      edge[a].push_back(tmp);
      tmp.next = a;
      edge[b].push_back(tmp);
    }
    scanf("%d%d", &S, &T);

    // init
    for (int i=1; i<=n; i++){
      dist[i] = -1;
      mark[i] = false;
    }
    dist[S] = 0;
    mark[S] = true;
    int new_v = S;
    for (int i=1; i<n; i++){
      for (int j=0; j<edge[new_v].size(); j++){
        int t = edge[new_v][j].next;
        int c = edge[new_v][j].c;
        int co = edge[new_v][j].cost;
        if (mark[t] == true) continue;
        // MARK: !!! core !!! to update the dist and cost
        if (dist[t] == -1 || dist[t] > dist[new_v]+c ||\
            (dist[t] == dist[new_v]+c && cost[t] > cost[new_v] + co)){
          dist[t] = dist[new_v] + c;
          cost[t] = cost[new_v] + co;
        }
      }





      // get the min of visited vertex in dist
      int min = 1231231234;
      for (int j=1; j<=n; j++){
        if (mark[j] == true) continue;
        if (dist[j] == -1) continue;
        if (dist[j] < min){
          min = dist[j];
          new_v = j;
        }
      }
      mark[new_v] = true;
    }
    printf("%d%d\n", dist[T], cost[T]);
  }
  return 0;
}
