// 1003 Emergency with cpp
// the same version as Wangdao from internet

#include <cstdio>
#include <vector>
using namespace std;
struct Edge {
    int next;
    int c;
};
vector<Edge> edge[502];
int Dis[502];
bool mark[502];
int paths[502]; //paths[]是记录起点到各个点的最短路径数目的
int nums[502]; //nums[]是当前城市的救援队伍数目的
int all_nums[502]; //all_nums[]是记录从起点到当前点的总救援队伍数目的

int main(void)
{
    int i, j, n, m, s, e;
    while (scanf("%d %d %d %d", &n, &m, &s, &e) != EOF) {
        for (i = 0; i < n; i++) {
            edge[i].clear();
            Dis[i] = -1;
            mark[i] = false;
            paths[i] = 0;
            nums[i] = 0;
            all_nums[i] = 0;
            scanf("%d", &nums[i]);
        }
        for (i = 0; i < m; i++) { //输入图
            int a, b, c;
            scanf("%d %d %d", &a, &b, &c); // c 边权
            Edge tmp;
            tmp.c = c;
            tmp.next = b;
            edge[a].push_back(tmp);
            tmp.next = a;
            edge[b].push_back(tmp);
        }
        Dis[s] = 0;
        mark[s] = true;
        all_nums[s] = nums[s];
        int newP = s;
        paths[newP] = 1;
        for (i = 0; i < n; i++) {
            for (j = 0; j < edge[newP].size(); j++) {
                int t = edge[newP][j].next;
                int c = edge[newP][j].c;
                if (mark[t] == true) continue;
                // MARK: !!! core !!! to update the dist and cost
                if (Dis[t] == -1 || Dis[newP] + c < Dis[t]) {
                    paths[t] = paths[newP];
                    Dis[t] = Dis[newP] + c;
                    all_nums[t] = all_nums[newP] + nums[t];
                }
                else if (Dis[t] == Dis[newP] + c) { // 如果路径的距离相同，
                    paths[t] += paths[newP];
                    if (all_nums[t] < all_nums[newP] + nums[t]) //选择点权更大的。注意，如果这里使用了 all_nums[t] < all_nums[newP] + nums[t]， 则下面输出的时候不加nums[e]
                        all_nums[t] = all_nums[newP] + nums[t];
                }
            }
            // get the min of non-visited vertex in Dis
            int min = 1 << 30;
            for (j = 0; j < n; j++) {
                if (mark[j] == true) continue;
                if (Dis[j] == -1) continue;
                if (Dis[j] < min) {
                    min = Dis[j];
                    newP = j;
                }
            }
            mark[newP] = true;
        }
        printf("%d %d\n", paths[e], all_nums[e]);
    }
    return 0;
}
