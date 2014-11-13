//============================================================================
// Name        : HexToBase64.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdio.h>
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

int main() {
	string input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
	for( unsigned int i = 0; i < input.length(); i++ ){
		cout << input[i] << " " << hexToDecimal(input[i]) << endl;
	}
	//hexToDecimal(input);
	//cout << input << endl;
	return 0;
}
