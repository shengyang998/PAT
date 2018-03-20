/**
 * This file consist the C++11 code to solve "PAT 1141 PAT Ranking of Institutions". 
 * The idea is: 
 * 		1. init an unordered_map of <school_name, School>; 
 * 		2. load data to the map (Complexity: O(N)); 
 * 		3. convert the map to a vector (Complexity: O(N));
 * 		4. sort with costumized function (Complexity: O(NlogN) or worst: O(N^2));
 * 		5. output the vector as the output specification (Complexity: O(N));
 * 		
 * The description of the question is shown below:
 * 
 * 1141. PAT Ranking of Institutions (25)
 * 时间限制
 * 500 ms
 * 内存限制
 * 65536 kB
 * 代码长度限制
 * 16000 B
 * 判题程序
 * Standard
 * 作者
 * CHEN, Yue
 * 
 * After each PAT, the PAT Center will announce the ranking of institutions based on their students' performances. Now you are asked to generate the ranklist.
 * Input Specification:
 * Each input file contains one test case. For each case, the first line gives a positive integer N (<=105), which is the number of testees. Then N lines follow, each gives the information of a testee in the following format:
 * ID Score School
 * where "ID" is a string of 6 characters with the first one representing the test level: "B" stands for the basic level, "A" the advanced level and "T" the top level; "Score" is an integer in [0, 100]; and "School" is the institution code which is a string of no more than 6 English letters (case insensitive). Note: it is guaranteed that "ID" is unique for each testee.
 * Output Specification:
 * For each case, first print in a line the total number of institutions. Then output the ranklist of institutions in nondecreasing order of their ranks in the following format:
 * Rank School TWS Ns
 * where "Rank" is the rank (start from 1) of the institution; "School" is the institution code (all in lower case); "TWS" is the total weighted score which is defined to be the integer part of "ScoreB/1.5 + ScoreA + ScoreT*1.5", where "ScoreX" is the total score of the testees belong to this institution on level X; and "Ns" is the total number of testees who belong to this institution.
 * The institutions are ranked according to their TWS. If there is a tie, the institutions are supposed to have the same rank, and they shall be printed in ascending order of Ns. If there is still a tie, they shall be printed in alphabetical order of their codes.
 * 
 * Sample Input:
 * 10
 * A57908 85 Au
 * B57908 54 LanX
 * A37487 60 au
 * T28374 67 CMU
 * T32486 24 hypu
 * A66734 92 cmu
 * B76378 71 AU
 * A47780 45 lanx
 * A72809 100 pku
 * A03274 45 hypu
 * 
 * Sample Output:
 * 5
 * 1 cmu 192 2
 * 1 au 192 3
 * 3 pku 100 1
 * 4 hypu 81 2
 * 4 lanx 81 2
 *
 * 
 */
#include<iostream>
#include<string>
#include<algorithm>
#include<unordered_map>
#include<vector>
using namespace std;

//#define DEBUG
namespace My {
#ifdef DEBUG
	long cntlog = 0;
	template <class Tp>
	inline void log(Tp x, string lv = "INFO") {
		My::cntlog++;
		std::cout << "--> " << lv << " " << x << std::endl;
	}
#endif
#ifndef DEBUGs
	template <class Tp>
	inline void log(Tp x, ...) {}
#endif
}

class School { // Class for saving status of each institution
	string name;
	int counter;
	double score;
	long sc; // save time, for the convertion from double to long is somehow expensive
public:
	School(string &name, double score, char level) {
		this->name = name;
		this->counter = 0;
		this->score = 0;
		this->sc = -1;
		this->append(score, level);
	}
	School* append(double score, char level) {
		this->counter++;
		double lv = 1.0;
		if (level == 'B')
			lv = 2.0 / 3.0;
		else if (level == 'T')
			lv = 1.5;
		this->score += score * lv;
		return this;
	}
	int get_counter() const {
		return this->counter;
	}
	long long get_score() {
		if(this->sc == -1){
			this->sc = long(this->score);	// In the test case as the `Sample Input`, this line will be hit 5 times
		}
		return this->sc;					// and this line will be hit 49 times. So this `lazy initial tech` should save some time.
	}
	string get_name() const {
		return this->name;
	}
};

class Result { // Class for saving the result, containing an unordered map of <school name, School>
	unordered_map <string, School*> d;
public:
	void append(string school_name, int score, char level) {
		if (d.find(school_name) == d.end())
			d.insert(pair <string, School*> (school_name, new School(school_name, score, level)));
		else
			d[school_name]->append(score, level);
	}
	vector<pair<string, School*>>& sort() { // sort function. use a lambda to costumize, and return a sorted vector
		auto cmp = [&](const pair <string, School*> &lhs, const pair <string, School*> &rhs) -> bool {
			if (lhs.second->get_score() == rhs.second->get_score()) {
				if (lhs.second->get_counter() == rhs.second->get_counter())
					return lhs.second->get_name() < rhs.second->get_name();
				else
					return lhs.second->get_counter() < rhs.second->get_counter();
			} else{
				return lhs.second->get_score() > rhs.second->get_score();
			}
		};
		vector<pair<string, School*>> *vec = new vector<pair<string, School*>>(this->d.begin(), this->d.end());
		std::sort(vec->begin(), vec->end(), cmp);
		return *vec;
	}
};

int main() {
	int N;
	cin >> N;
	Result* res = new Result();
	while (N--) {
		char level[7];
		int score;
		string name;
		cin >> level >> score >> name;
		char lv = level[0];
		transform(name.begin(), name.end(), name.begin(), ::tolower); 	// transform the school name to lower case
		res->append(name, score, lv);									// append to the result (as an unordered map)
	}
	vector<pair<string, School*>> r = res->sort();						// sort the result and return a vector
	unsigned long n = r.size();
	cout << n << endl;
	unsigned long cnt = 1, i = 0;
	for (auto iter = r.begin(); iter != r.end(); iter++) {
		i++;
		if (iter != r.begin() and iter->second->get_score() != (iter - 1)->second->get_score()) { // calculate the rank of each institution (Complexity: O(1), so the outter for loop is O(N))
			cnt = i;
		}
		cout << cnt << " " << iter->second->get_name() << " " << iter->second->get_score() << " " << iter->second->get_counter() << endl;
	}
	return 0;
}
