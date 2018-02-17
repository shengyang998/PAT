#include<cstdio>
using namespace std;
#define LL long long

class Date{
  int dayOfMonth_table[13][2] = {
    0,0,
    31,31,
    28,29,
    31,31,
    30,30,
    31,31,
    30,30,
    31,31,
    31,31,
    30,30,
    31,31,
    30,30,
    31,31
  };
public:
  int year;
  int month;
  int day;
  bool isLeap(LL arg){
    return (arg % 100 != 0 && arg % 4 == 0) || arg % 400 == 0? true : false;
  }
  int dayOfMonth(int m, int y){
    return dayOfMonth_table[m][isLeap(y)];
  }
  void nextDay(){
    day++;
    if (day > dayOfMonth(month, year)){
	day = 1;
	month++;
	if (month > 12){
	  month = 1;
	  year++;
	}
    }
  }
};

LL abs(LL x){
  return x < 0 ? -x : x;
}

int main(){
  int buf[65530][13][32];
  Date tmp;
  int cnt = 0;
  tmp.day = 1;
  tmp.month = 1;
  tmp.year = 0;
  while(tmp.year != 65530){
    buf[tmp.year][tmp.month][tmp.day] = cnt;
    tmp.nextDay();
    cnt++;
  }
  int d1, m1, y1;
  int d2, m2, y2;
  while(scanf("%4d%2d%2d", &y1, &m1, &d1)){
    scanf("%4d%2d%2d", &y2, &m2, &d2);
    printf("%lld\n", abs(buf[y2][m2][d2] - buf[y1][m1][d1]));
  }
  return 0;
}
