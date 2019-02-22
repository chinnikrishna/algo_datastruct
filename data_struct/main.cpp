#include <iostream>
#include "list.h"
#include "stack.h"

using namespace std;

int main(){
    List A;
    A.insNode(10);
    A.insNode(20);
    A.insNode(40);
    A.insNode(50, -1);
    A.insNode(23, 2);
    A.insNode(34, 1);
    A.printList();
    A.delNode(1);
    A.printList();
	
	Stack S(20);
	S.Push(24);
	S.Push(32);
	S.Push(67);
	S.Pop();
	S.Pop();
	S.Pop();
	S.Pop();    
}
