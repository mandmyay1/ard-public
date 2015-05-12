/*
 * Node.cpp
 *
 *  Created on: Nov 24, 2014
 *      Author: Adam
 */

#include "Node.h"


Node::Node(int val): right(NULL), left(NULL), payload(val) {
	// TODO Auto-generated constructor stub

}

Node::~Node() {
	// TODO Auto-generated destructor stub
}


int main(int argc, char **argv){
	Tree t;
	t.insert(1).insert(2);
}
