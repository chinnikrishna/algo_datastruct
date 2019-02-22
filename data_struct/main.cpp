#include <iostream>
#include "list.h"
#include "stack.h"
#include "double_list.h"

using namespace std;

void tempfunc(){
    List A;
    A.insNode(10);
    A.insNode(20);
    A.insNode(40);
    A.insNode(50, -1);
    A.insNode(23, 2);
    A.insNode(34, 1);
    A.printList();
    A.revList();
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

int main(){
    
    DoubleList DList;
    DList.insNode(23);
    DList.insNode(57);
    DList.insNode(90, -1);
    DList.insNode(48, -1);
    DList.insNode(56, 1);
    DList.printList();
    DList.delNode(1);
    DList.printList();
}
