#include "header.h"


// constructor for terminator stack
stack::stack(): head(NULL){


};

inline void stack::push(const unsigned int& data){
    node* new_head = new node;
    new_head->data = data;
    new_head->next = this->head;
    this->head = new_head;
};

unsigned int stack::pop(){

};  

void stack::clear(){
    
    
};
