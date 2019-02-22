#ifndef STACK
#define STACK
#include "list.h"

class Stack {
private:
	int maxSize;
	List Stk;
public:
	Stack(int StkSize=10);
	void Pop();
	void Push(int data);
	bool isFull();
	bool isEmpty();
};
#endif
