/*
 * Node.h
 *
 *  Created on: Nov 24, 2014
 *      Author: Adam
 */

#ifndef NODE_H_
#define NODE_H_


class Node {
public:
	Node *right;
	Node *left;
	int payload;
	Node(int val);
	~Node();
};
class Tree {
private:
	Node *root;
public:
	Tree();
	virtual ~Tree();
	Tree& insert(int val);
};


#endif /* NODE_H_ */
