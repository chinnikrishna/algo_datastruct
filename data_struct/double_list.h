#ifndef DOUBLE_LIST
#define DOUBLE_LIST
class DoubleList{
private:
    typedef struct Node{
        int data;
        Node* next;
        Node* prev;
    }* nodePtr;
    nodePtr curr, temp, head, tail;
    
public:
    DoubleList();
    void insNode(int newData, int pos=0);
    void delNode(int pos=0);
    int listLen();
    void printList();
};
#endif