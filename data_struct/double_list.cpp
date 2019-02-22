#include <iostream>
#include "double_list.h"

using namespace std;

DoubleList::DoubleList(){
    head=NULL;
    curr=NULL;
    temp=NULL;
    tail=NULL;
}

int DoubleList::listLen(){
    if(head != NULL){
        int len = 0;
        curr = head;
        while(curr->next != NULL){
            len++;
            curr = curr->next;
        }
        len++;
        return len;
    }
    else
        return 0;
}

void DoubleList::printList(){
    if(head!=NULL){
        curr=head;
        while(curr->next != NULL){
            cout<<"|"<<curr->data;
            curr = curr->next;
        }
        cout<<"|"<<curr->data<<"|"<<endl;
    }
    else
        cout<<"Empty List"<<endl;
}

void DoubleList::delNode(int pos){
    if(pos == 0){
        curr = head;
        head = curr->next;
        delete curr;
    }
    else if(pos == -1){
        curr = tail;
        tail = curr->prev;
        delete curr;
    }
    else{
        if(pos <= listLen()){
            int posCount=0;
            curr = head;
            while(posCount < pos){
                posCount++;
                temp = curr;
                curr = curr->next;
            }
            temp->next = curr->next;
            curr->next->prev = temp;
            delete curr;
        }
        else
            cout<<"Given node out of range"<<endl;
    }
}

void DoubleList::insNode(int newData, int pos){
    nodePtr n = new Node;
    n->data = newData;
    n->next = NULL;
    n->prev = NULL;
    
    if(pos == 0){
        if(head != NULL){
            curr = head;
            head = n;
            curr->prev = head;
            head->next = curr;
        }
        else{
            head=n;
            tail=n;
        }
    }
    else if(pos == -1){
        if(head != NULL){
            tail->next = n;
            n->prev = tail;
            tail = n;
        }
        else{
            head=n;
            tail=n;
        }
    }
    else{
        if(pos <= listLen()){
            int posCount = 0;
            curr=head;
            while(posCount < pos){
                posCount++;
                temp = curr;
                curr = curr->next;
            }
            temp->next = n;
            n->prev = temp;
            n->next = curr;
            curr->prev = n;            
        }
        else
            cout<<"Given node out of range"<<endl;
    }
}
    