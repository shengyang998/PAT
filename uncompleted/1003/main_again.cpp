#include<cstdio>
#include<vector>
#include<algorithm>
#define MAX_LEN 502
using namespace std;
struct E{
  int next;
  int cost;
};
vector<E> edge[MAX_LEN];
int dist[MAX_LEN];
bool mark[MAX_LEN];
int dist_cnt[MAX_LEN];
int weight[MAX_LEN];
int max_weight[MAX_LEN];

int main(){
  int n, m, source, target; // n vertexes, m edges
  // init vertexes
  while(scanf("%d %d %d %d", &n, &m, &source, &target)!=EOF){
    for(int i=0; i<n; i++){
      scanf("%d", &weight[i]);
      edge[i].clear();
      dist[i] = -1;
      mark[i] = false;
      dist_cnt[i] = 0;
      max_weight[i] = 0;
    }
    // init edges
    for(int i=0; i<m; i++){
      int a, b, c;
      scanf("%d %d %d", &a, &b, &c);
      E tmp;
      tmp.cost = c;
      tmp.next = b;
      edge[a].push_back(tmp);
      tmp.next = a;
      edge[b].push_back(tmp);
    }
    dist[source] = 0;
    mark[source] = true;
    dist_cnt[source] = 1;
    max_weight[source] = weight[source];
    int p = source;
    for(int i=0; i<n; i++){
      for(int j=0; j<edge[p].size(); j++){
        int t = edge[p][j].next;
        int c = edge[p][j].cost; // cost of edges
        if(mark[t] == true) continue; // MARK: mark[t] not mark[j]!!! don't make it wrong
        if(dist[t] == -1 || dist[t] > dist[p] + c){
          dist[t] = dist[p] + c;
          dist_cnt[t] = dist_cnt[p];
          max_weight[t] = max_weight[p] + weight[t];
        }
        else if(dist[t] == dist[p] + c){
          dist_cnt[t] += dist_cnt[p];
          if(max_weight[t] < max_weight[p] + weight[t])
            max_weight[t] = max_weight[p] + weight[t];
        }
      }
      int min = 1<<30;
      for(int j=0; j<n; j++){
        if(mark[j] == true) continue;
        if(dist[j] == -1) continue;
        if(dist[j] < min){
          min = dist[j];
          p = j;
        }
      }
      mark[p] = true;
    }
    printf("%d %d\n", dist_cnt[target], max_weight[target]);
  }
  return 0;
}
