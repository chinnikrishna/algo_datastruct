#include <iostream>
#include "list.h"

using namespace std;


//Constructor
List::List(){
    head=NULL;
    curr=NULL;
    temp=NULL;
}


//List length
int List::listLen(){
    int len=0;
    curr=head;
    while(curr->next != NULL){
        len++;
        curr=curr->next;
    }
    len++;
    return len;
}


//Print Data
void List::printList(){
    if(head!=NULL){
        curr=head;
        while(curr->next!=NULL){
            cout<<"|"<<curr->data;
            curr = curr->next;
        }
        cout<<"|"<<curr->data<<"|"<<endl;
    }
    else
        cout<<"Empty List"<<endl;
}


//Insert Data
void List::insNode(int newData, int pos){
    nodePtr n = new Node();
    n->data = newData;
    n->next = NULL;
    
    //Insert at the start
    if(pos == 0){
        if(head != NULL){
            curr=head;
            head=n;
            n->next = curr;
        }
        else
            head=n;
    }
    //Insert at the end
    else if(pos == -1){
        if(head != NULL){
            curr=head;
            while(curr->next != NULL)
                curr = curr->next;
            curr->next = n;
        }
        else
            head=n;
    }
    //Insert at a position
    else{
        int len = listLen();
        if(pos <= len){
            int posCount=0;
            curr=head;
            while(posCount != pos){
                temp = curr;
                curr = curr->next;
                posCount++;
            }
            temp->next = n;
            n->next=curr;
        }
        else
            cout<<"Given node out of range"<<endl;
    }   
}

void List::delNode(int pos){
    //Remove the first node
    if(pos == 0){
        curr=head;
        head = curr->next;
        delete curr;
    }
    else if(pos == -1){
        curr=head;
        while(curr->next != NULL){
            temp = curr;
            curr = curr->next;            
        }
        temp->next = NULL;
        delete curr;
    }
    else{
        int len = listLen();
        if(pos <= len){
            int posCount = 0;
            curr = head;
            while(posCount != pos){
                temp =  curr;
                curr = curr->next;
                posCount++;
            }
            temp->next = curr->next;
            delete curr;
        }
        else
            cout<<"Given node out of range"<<endl;
    }
}

//Returns the pointer of a node
nodePtr List::getNode(int pos){
    if(pos == 0)
        return head;
    else if(pos == -1){
        curr = head;
        while(curr->next != NULL)
            curr = curr->next;
        return curr;
    }
    else{
        if(pos <= listLen()){
            int posCount = 0;
            while(posCount < pos){
                curr = curr->next;
                posCount++;
            }
            return curr;
        }
        else{
            cout<<"Given node out of range"<<endl;
            return NULL;
        }
    }
    
}
