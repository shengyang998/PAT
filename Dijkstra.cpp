// Normal Dijkstra with cpp

#include<cstdio>
#include<vector>
using namespace std;
struct E{
  int next;
  int c;
};
vector<E> edge[101]; // an array of vector<E>, to storage the edges
bool mark[101]; // mark the vertex if it has been visited
int dist[101];
int main(){
  int n, m;
  while (scanf("%d%d", &n, &m)!=EOF){
    if (n == 0 && m == 0) break;
    // init
    for (int i = 1; i<=n; i++){
      edge[i].clear()
    }
    // get graph
    while(m--){
      int a, b, c;
      scanf("%d%d%d", &a, &b, &c);
      E tmp;
      tmp.c = c;
      tmp.next = b;
      edge[a].push_back(tmp);
      tmp.next = a;
      edge[b].push_back(tmp);
    }
    // init
    for(int i = 1; i<=n; i++){
      dist[i] = -1;
      mark[i] = false;
    }
    dist[1] = 0;
    mark[1] = true;
    int new_v = 1;
    // init completed
    // core bellow:
    for (int i=1; i<n; i++){ // for each vertex of graph
      for(int j=0; j<edge[new_v].size(); j++){ // for each vertex which linked to the above vertex
        int t = edge[new_v][j].next;
        int c = edge[new_v][j].c;
        if(mark[t] == true) continue;
        // MARK: !!! core !!! to update the dist
        if(dist[t] == -1 || dist[t] > dist[new_v] + c)
          dist[t] = dist[new_v] + c;
      }



      // get the min of non-visited vertex in dist
      int min = 123123123;
      for(int j = 1; j<=n; j++){
        if(mark[j] == true) continue;
        if(dist[j] == -1) continue;
        if(dist[j] < min){
          min = dist[j];
          new_v = j; // new_v = min(dist, lambda x: x[1])
        }
      }
      mark[new_v] = true;
    }
    printf("%d\n", dist[n]);
  }
  return 0;
}
