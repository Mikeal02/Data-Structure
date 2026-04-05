/*
 * DATE: April 5, 2026
 * PATTERN: Doubly Linked List
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Rebuild list from vector including new value at end.
 * - TIME: O(n) | SPACE: O(n)
 *
 * 2. BETTER:
 * - Step 1: Walk to tail, append new node, set both next and back links.
 * - TIME: O(n) to find tail | SPACE: O(1)
 *
 * 3. OPTIMAL:
 * - Step 1: Keep tail pointer for O(1) insert at end; without tail, walk is required once.
 * - TIME: O(n) without tail | SPACE: O(1)
 *
 * AHA-MOMENT: Tail insertion in DLL is four pointer writes—prev of new, next of old tail, etc.
 */

#include<bits/stdc++.h>
using namespace std;

class Node
{
    public:
    int val;
    Node * next;
    Node * back;

    Node(int val1,Node* next1,Node* back1)
    {
        val=val1;
        next=next1;
        back=back1;

    }
    Node(int val1)
    {
        val=val1;
        next=nullptr;
        back=nullptr;
    }
};

class Solution
{
    public:
    Node * insert_in_DLL(Node* head,int key)
    {
        Node* newNode=new Node(key);
        if(head==nullptr)return newNode;
        Node * temp=head;
        while(temp->next!=nullptr)
        {
            temp=temp->next;

        }
        temp->next=newNode;
        newNode->back=temp;
        return head;
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
    
    Node * convert_arr_2DLL(vector<int>& arr)
    {
        Node * head=new Node(arr[0]);
        Node * prev=head;

        for(int i=0;i<arr.size();i++)
        {
            Node * temp=new Node(arr[i],nullptr,prev);
            prev->next=temp;
            prev=temp;
        }
        return head;
    }
};

int main()
{
    Solution sol;
    vector<int> arr={12,5,8,7,4};
    Node* head=convert_arr_2DLL(arr);

    cout<<"Doubly Linked List Initially:"<<endl;

    sol.printList(head);

    head=sol.insert_in_DLL(head,55);

    cout<<"Doubly Linked List After Inserting at tail:"<<endl;
    sol.printList(head);

    return 0;


}


