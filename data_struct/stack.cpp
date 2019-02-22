#include <iostream>
#include "stack.h"

using namespace std;
Stack::Stack(int stkSize){
	maxSize=stkSize;
}

bool Stack::isFull(){
	bool full = (Stk.listLen() == maxSize);
	return full;
}

bool Stack::isEmpty(){
	bool empty = (Stk.listLen() == 0);
	return empty;
}

void Stack::Push(int data){
	if (!(Stack::isFull())){
		Stk.insNode(data);
		Stk.printList();
	}
	else
		cout<<"Stack is full"<<endl;
}

void Stack::Pop(){
	if (!(Stack::isEmpty())){
		Stk.delNode();
		Stk.printList();
	}
	else
		cout<<"Stack is Empty"<<endl;
}
	
	
	