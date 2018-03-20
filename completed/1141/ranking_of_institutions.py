"""
This file consist the python3 code to solve "PAT 1141 PAT Ranking of Institutions" partially.
The idea is: 
	1. init an dictionary of <school_name, School>; 
	2. load data to the dict (Complexity: O(N)); 
	3. sort the dictionary with costumized key and convert to a list which is automatically done by the default sort() function (Complexity: O(2NlogN) or worst: O(2N^2));
	4. output the list as the output specification;

The description of the question is shown below:

1141. PAT Ranking of Institutions (25)
时间限制
500 ms
内存限制
65536 kB
代码长度限制
16000 B
判题程序
Standard
作者
CHEN, Yue

After each PAT, the PAT Center will announce the ranking of institutions based on their students' performances. Now you are asked to generate the ranklist.
Input Specification:
Each input file contains one test case. For each case, the first line gives a positive integer N (<=105), which is the number of testees. Then N lines follow, each gives the information of a testee in the following format:
ID Score School
where "ID" is a string of 6 characters with the first one representing the test level: "B" stands for the basic level, "A" the advanced level and "T" the top level; "Score" is an integer in [0, 100]; and "School" is the institution code which is a string of no more than 6 English letters (case insensitive). Note: it is guaranteed that "ID" is unique for each testee.
Output Specification:
For each case, first print in a line the total number of institutions. Then output the ranklist of institutions in nondecreasing order of their ranks in the following format:
Rank School TWS Ns
where "Rank" is the rank (start from 1) of the institution; "School" is the institution code (all in lower case); "TWS" is the total weighted score which is defined to be the integer part of "ScoreB/1.5 + ScoreA + ScoreT*1.5", where "ScoreX" is the total score of the testees belong to this institution on level X; and "Ns" is the total number of testees who belong to this institution.
The institutions are ranked according to their TWS. If there is a tie, the institutions are supposed to have the same rank, and they shall be printed in ascending order of Ns. If there is still a tie, they shall be printed in alphabetical order of their codes.

Sample Input:
10
A57908 85 Au
B57908 54 LanX
A37487 60 au
T28374 67 CMU
T32486 24 hypu
A66734 92 cmu
B76378 71 AU
A47780 45 lanx
A72809 100 pku
A03274 45 hypu

Sample Output:
5
1 cmu 192 2
1 au 192 3
3 pku 100 1
4 hypu 81 2
4 lanx 81 2
"""

# DEBUG = True
# def log(msg, lv='INFO'):
# 	if DEBUG==True:
# 		print("{0}: {1}".format(lv, msg))

class School:
	name = ''
	score = 0
	counter = 0
	def __init__(self, school_name, score, level):
		self.name = school_name
		self.append(score, level)

	def append(self, score, level):
		self.counter += 1
		lv = 1
		if level == 'B':
			lv = 2/3
		elif level == 'T':
			lv = 1.5
		self.score += score * lv
		return self

	def set_score_to_int(self):
		self.score = int(self.score)
		return self


if __name__ == '__main__':
	s = int(input())
	d = {}
	for i in range(s):
		t = input().split(' ')
		level = t[0][0]
		score = int(t[1])
		school_name = t[2].lower()
		if school_name in d.keys():
			d[school_name].append(score, level)
		else:
			d[school_name] = School(school_name, score, level)
	d = sorted(d.items(), key=lambda x: [-x[1].score, x[1].counter, x[0]])	# Could cost most of the time
	print(len(d))
	cnt = 1
	for i in range(len(d)):
		if i > 0 and int(d[i][1].score) != int(d[i-1][1].score):
			cnt = i+1
		print("{0} {1} {2} {3}".format(cnt, d[i][1].name, int(d[i][1].score), d[i][1].counter))
