#include <iostream>
#include <memory>


typedef struct node{
    unsigned int data; // data variable, EXPANDED from char to include more symbols
    node* next; // next
};


class stack{
    public:
    node* head;
    stack();

    inline void push(const unsigned int& data); //pushes to stack
    unsigned int pop(); //pops from stack
    inline void clear(); // clears the stack
    
};