#include<bits/stdc++.h>
using namespace std;

class Node
{
    public:
    int val;
    Node* next;

    Node(int val1, Node* next1)
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
    Node* delete_node(Node *head)
    {
        if(head==nullptr || head->next==nullptr)
        {
            delete head;
            return nullptr;

        }
        Node * temp=head;
        while(temp->next->next!=nullptr)
        {
            temp=temp->next;
        }
        Node * drop= temp->next;
        temp->next=nullptr;
        delete drop;
        return head;

    }

    void printList(Node * head)
    {
        Node * temp=head;
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
    Node * head=new Node(1);
    head->next=new Node(2);
    head->next->next=new Node(3);
    head->next->next->next=new Node(4);

    sol.printList(head);

    head=sol.delete_node(head);

    sol.printList(head);

}