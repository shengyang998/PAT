/*
 * main.cpp
 *
 *  Created on: 2017年1月21日
 *      Author: ysy
 *  Public Bike Management
 */
#include<iostream>
#include<string>
using namespace std;

// 方案一，不使用标准库函数，自己写转换方法

// 获取非负整数的位数
int getLengthFromPositiveInt(int num){
	int length = 1;
	while(1){
		if (num /= 10) length++;
		else break;
	}
	return length;
}

// 获取负整数的位数
int getLengthFromNagetiveInt(int num){
	num = -num;
	int result = getLengthFromPositiveInt(num);
	return result + 1;// 1为符号位
}

// 获取整数的位数
int getLengthFromInt(int num){
	if(num < 0){
		return getLengthFromNagetiveInt(num);
	}else{
		return getLengthFromPositiveInt(num);
	}
}

char* formattedStringFromInt(int num){
	int numLength = getLengthFromInt(num) + getLengthFromInt(num)/3;
	char* number = new char[numLength];
	if(num < 0){
		number[0] = '-';
		num = -num;
	}
	for(int i=numLength-1; i>0; i--){
		if((numLength-i)%4 == 0){
			number[i] = ',';
			continue;
		}else{
			number[i] = num%10 + 48;
			num /= 10;
		}
	}
	return number;
}

int main(){
    int numA, numB;
    cin>>numA>>numB;
    int result = numA+numB;
    cout<<"The result is "<<result<<endl;
    cout<<"The Length of the result is "<<getLengthFromInt(result)<<endl;
    cout<<"The formatted result is "<<formattedStringFromInt(result)<<endl;
    return 0;
}
