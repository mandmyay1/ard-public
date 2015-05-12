//============================================================================
// Name        : HexToBase64.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
#include <set>
//#include <unordered_set>
using namespace std;

int hexToDecimal(char inputHex){
	if( '0' <= inputHex && inputHex <= '9' ){
		return inputHex - '0';
	}
	else if( 'a' <= inputHex && inputHex < 'z' ){
		return inputHex - 'a' + 10;
	}
	return inputHex - 'A' + 10;
}

bool hasUnique(char *iString){
	set<char> occurences;
	char *iter = iString;
	while( *iter != '\0'){
		char oneChar = *iter;
		if( occurences.find(oneChar) != occurences.end()){
			return false;
		}
		occurences.insert(oneChar);
		iter++;
	}
	return true;
}

bool hasUnique2(char *iString){
	char *iter1 = iString;
	char *iter2 = iString;
	while( *iter1 != '\0' ){
		iter2 = iter1+1;
		while( *iter2 != '\0' ){
			if( *iter2 == *iter1 ){
				return false;
			}
			iter2++;
		}
		iter1++;
	}
	return true;
}

void reverse(char *str){
	char *end = str;
	char tmp;
	while (*end != '\0' ){
		end++;
	}
	end--;
	while( str < end ){
		cout << str << " " << end << endl;
		tmp = *str;
		cout << 1 << endl;
		cout << *end << endl;
		cout << *str++ << endl;
		*str++ = *end;
		cout << 2 << endl;
		*end-- = tmp;
		cout << 3 << endl;
	}
}

int main() {
	string input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
	for( unsigned int i = 0; i < input.length(); i++ ){
		cout << input[i] << " " << hexToDecimal(input[i]) << endl;
	}
	char *pointer = NULL;
	char *input2 = "abcdefghijklmnopqrstuvwxyz";
	if( hasUnique(input2)){
		cout << "input2 unique" << endl;
	}
	else{
		cout << "input2 not unique" << endl;
	}
	char *input3 = "abcdefghijklmnopqrstuvwxyzabc";
	if( hasUnique(input3)){
		cout << "input3 unique" << endl;
	}
	else{
		cout << "input3 not unique" << endl;
	}


	if( hasUnique2(input2)){
		cout << "input2 unique2" << endl;
	}
	else{
		cout << "input2 not unique2" << endl;
	}
	if( hasUnique2(input3)){
		cout << "input3 unique2" << endl;
	}
	else{
		cout << "input3 not unique2" << endl;
	}

	reverse(input3);
	cout << input3 << endl;
	//hexToDecimal(input);
	//cout << input << endl;
	return 0;
}
