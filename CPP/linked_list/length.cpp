/*
 * DATE: April 5, 2026
 * PATTERN: Linked List Traversal
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Copy to array while traversing, return array size.
 * - TIME: O(n) | SPACE: O(n)
 *
 * 2. BETTER:
 * - Step 1: Recursive length (stack depth n).
 * - TIME: O(n) | SPACE: O(n) call stack
 *
 * 3. OPTIMAL:
 * - Step 1: Iterative counter while walking next pointers until null.
 * - TIME: O(n) | SPACE: O(1)
 *
 * AHA-MOMENT: Length is one pass with a counter—no extra structure needed.
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