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
    // O(n),O(1)
    int length_LL(Node* head)
    {
        Node* temp=head;
        int length=0;
        while(temp!=nullptr)
        {
            length++;
            temp=temp->next;
        }
        return length;
    }
};

int main()
{
    Solution sol;
    Node* head=new Node(2);
    head->next=new Node(3);
    head->next->next=new Node(4);
    head->next->next->next=new Node(5);

    cout<<"The length of LL is "<<sol.length_LL(head);
    return 0;


}