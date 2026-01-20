#include<bits/stdc++.h>
using namespace std;

class Node
{
    public:
    int val;
    Node * next;

    Node(int val1,Node* next1)
    {
        val=val1;
        next=next1;

    }
    Node(int val1)
    {
        val=val1;
        next=nullptr;
    }
};

class Solution
{
    public:
    Node* insert_at_head(Node*head, int newdata)
    {
        Node* newhead=new Node(newdata,head);
        return newhead;

    }

    void printList(Node* head)
    {
        Node* temp=head;
        while(temp!=nullptr)
        {
            cout<<temp->val<<" ";
            temp=temp->next;
        }
    }
};

int main()
{
    Solution sol;
    Node* head=new Node(2);
    head->next=new Node(3);
    head->next->next=new Node(4);

    cout<<"Before Insertion:"<<endl;
    sol.printList(head);

    head= sol.insert_at_head(head,6);
    cout<<"After Insertion:"<<endl;
    sol.printList(head);
    return 0;
    
}