#ifndef LIST
#define LIST
class List {

private:
    typedef struct Node{
        int data;
        Node* next;
    }* nodePtr;
    
    nodePtr head, curr, temp;
public:
    List();
    void insNode(int newData, int pos=0);
    void delNode(int pos=0);
    void revList();
    void printList();
    int listLen();
    //nodePtr getData(int pos=0);
};
    
#endif
