/*
 * main.cpp
 *
 *  Created on: 2017年3月2日
 *      Author: yjm
 *  Public Bike Management
 */
#include<iostream>
#include<fstream>
using namespace std;

/// 任务是找到时间最短，所需车辆最少的路径

class Node{
	int index; // 车站编号
	int currentC; // 当前容量
	int //
};

int getfile2int(ifstream& input){
	char str[12] = {0};
	input.getline(str, 12, ' ');
	return atoi(str);
}

int main(){

	// 初始化
	int CMAX = 0; // 单个车站最大容量
	int N = 0; // 车站总量(不包括管理中心)
	int sp = 0; // index of the problem station
	int M = 0; // number of roads

	ifstream inputFile;
	inputFile.open("input",ios::in);
	if (inputFile.fail()){
		cerr<<"Failed open"<<endl;
		return -1;
	}
	char tempStr[12];
	CMAX = getfile2int(inputFile);
	N = getfile2int(inputFile);
	sp = getfile2int(inputFile);
	M = getfile2int(inputFile);

	// 读取第二行
	int* C = new int[N]; // 每个站的当前车辆数目
	for (int i = 0; i<N; i++){
		C[i] = getfile2int(inputFile);
	}

	int* T = new int[M]; // 每条线路所花费的时间
	for (int i = 0; i<M; i++){
		T[i] = getfile2int(inputFile);
	}



	return 0;
}


