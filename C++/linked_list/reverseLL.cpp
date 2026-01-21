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
    
    Node * convert_arr_2LL(vector<int> &arr)
    {
        int n=arr.size();
        Node * head=new Node(arr[0]);
        Node * prev=head;
        for(int i=1;i<n;i++)
        {
            Node* temp=new Node(arr[i]);
            prev->next=temp;
            prev=temp;
        }
        return head;
    }
    // Iterative Approach: O(N)
    Node * reverseLL(Node * head)
    {
        Node * temp=head;
        Node * prev=nullptr;
        while(temp!=nullptr)
        {
            Node * curr=temp->next;
            temp->next=prev;
            prev=temp;
            temp=curr;
        }
        return prev;
    }

    // Recursive Approach:O(N)
    Node * reverseLL(Node * head)
    {
        if(head==nullptr || head->next==nullptr)return head;
        Node* newhead=reverseLL(head->next);
        Node * front=head->next;
        front->next=head;
        head->next=nullptr;

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
    vector<int> arr={2,3,4,5,6,7,8,9};
    Solution sol;
    Node * head=sol.convert_arr_2LL(arr);

    head=sol.reverseLL(head);
    sol.printList((head));
    return 0;
}