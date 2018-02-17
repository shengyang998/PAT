// 1003 Emergency with cpp
//

#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

struct E{
  int next;
  int cost;
};
vector<E> edge[502];
int dist[502];
int mark[502];
int dist_cnt[502];
int cost[502];
int max_cost[502];

int main(){
  int n, m, source, target;
  while(scanf("%d %d %d %d", &n, &m, &source, &target) != EOF){
    for(int i=0; i<n; i++){
      edge[i].clear();
      dist[i] = -1;
      mark[i] = false;
      dist_cnt[i] = 0;
      cost[i] = 0;
      max_cost[i] = 0;
      scanf("%d", &cost[i]); // input vertex and its cost
    }
    // input roads
    // using vector to imitate linked list
    for(int i=0; i<m; i++){
      int a, b, c;
      scanf("%d %d %d", &a, &b, &c);
      E tmp;
      tmp.cost = c;
      tmp.next = b;
      edge[a].push_back(tmp);
      tmp.next = a; // MARK: 转为无向图
      edge[b].push_back(tmp);
    }
    // MARK: init
    dist[source] = 0;
    mark[source] = true;
    dist_cnt[source] = 1;
    max_cost[source] = cost[source];
    int new_v = source; // new_v for new vertex
    for(int i=0; i<n; i++){
      for(int j=0; j<edge[new_v].size(); j++){
        int t = edge[new_v][j].next;
        int c = edge[new_v][j].cost;
        if(mark[t] == true) continue;
        if(dist[t] == -1 || dist[t] > dist[new_v] + c){
          dist[t] = dist[new_v] + c;
          dist_cnt[t] = dist_cnt[new_v];
          max_cost[t] = max_cost[new_v] + cost[t];
          // printf("max_cost[%d]=max_cost[%d]+cost[%d]=%d\n", t, new_v, t, max_cost[t]);
          // printf("                      %d       %d\n", max_cost[new_v], cost[t]);
        }
        else if(dist[t] == dist[new_v] + c){
          dist_cnt[t] += dist_cnt[new_v];
          if(max_cost[t] < max_cost[new_v] + cost[t])
            max_cost[t] = max_cost[new_v] + cost[t];
          // printf("max_cost[%d]=max_cost[%d]+cost[%d]=%d\n", t, new_v, t, max_cost[t]);
          // printf("                      %d       %d\n", max_cost[new_v], cost[t]);
        }
      }
      int min = 1<<30;
      for(int j=0; j<n; j++){
        if(mark[j] == true) continue;
        if(dist[j] == -1) continue;
        if(dist[j] < min){
          min = dist[j];
          new_v = j;
        }
      }
      mark[new_v] = true;
    }
    printf("%d %d\n", dist_cnt[target], max_cost[target]);
  }
  return 0;
}
