/*
 * DATE: April 5, 2026
 * PATTERN: Linked List, In-place Reversal
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Copy node values into a vector, reverse the vector, rebuild links—or use a stack of nodes.
 * - Step 2: Reassign next/back from rebuilt order.
 * - TIME: O(n) | SPACE: O(n) for auxiliary storage
 *
 * 2. BETTER:
 * - Step 1: Use a stack of node pointers; first pass push all nodes, second pass pop and relink in reverse.
 * - TIME: O(n) | SPACE: O(n) for stack
 *
 * 3. OPTIMAL:
 * - Step 1: Single traversal; at each node swap next and back (prev).
 * - Step 2: Move head to old tail via pointer walk.
 * - TIME: O(n) | SPACE: O(1) pointers only
 *
 * AHA-MOMENT: In a DLL, reversing is just swapping the two directions at every node—no extra structure needed.
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
    void printList(Node* head)
    {
        Node* temp=head;
        while(temp!=nullptr)
        {
            cout<<temp->val<<" ";
            temp=temp->next;
        }
        cout<<endl;
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

    // Brute Force Approach: O(n),O(n)
    Node * reverse_DLL(Node * head)
    {
        stack<int> st;
        Node* temp=head;
        while(temp!=nullptr)
        {
            st.push(temp->val);
            temp=temp->next;
        }

        temp=head;
        while(temp!=nullptr)
        {
            temp->val=st.top();
            st.pop();
            temp=temp->next;
        }

        return head;
    }
    // Optimal approach: O(n)
    Node * reverse_DLL(Node * head)
    {
        if(head==nullptr)return nullptr;
        if(head->next==nullptr)return head;
        Node * curr=head;
        while(curr!=nullptr)
        {
            Node* temp=curr->next;
            curr->next=curr->back;
            curr->back=temp;
            
            head=curr;
            curr=temp;

        }
        return head;

    }
};

int main()
{
    Solution sol;
    vector<int> arr={12,5,8,7,4};
    Node* head=sol.convert_arr_2DLL(arr);

    cout<<"Doubly Linked List Initially:"<<endl;

    sol.printList(head);

    head=sol.reverse_DLL(head);

    cout<<"Doubly Linked List After Inserting at tail:"<<endl;
    sol.printList(head);

    return 0;


}