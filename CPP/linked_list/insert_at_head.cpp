/*
 * DATE: April 5, 2026
 * PATTERN: Linked List, Sentinel / Head Insert
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Rebuild entire list with new element at front from array copy.
 * - TIME: O(n) | SPACE: O(n)
 *
 * 2. BETTER:
 * - Step 1: Create node and splice: newNode->next = head; return newNode as head.
 * - TIME: O(1) | SPACE: O(1) for one node
 *
 * 3. OPTIMAL:
 * - Same as better—insert at head is constant time for singly linked list.
 *
 * AHA-MOMENT: New head is just allocating one node and repointing a single pointer—no traversal.
 */

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