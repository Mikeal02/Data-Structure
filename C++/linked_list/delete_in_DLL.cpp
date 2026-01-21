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
    Node* convert_arr_2DLL(vector<int>& arr)
    {
        Node * head=new Node(arr[0]);
        Node * prev=head;

        for(int i=1;i<arr.size();i++)
        {
            Node * temp=new Node(arr[i],nullptr,prev);
            prev->next=temp;
            prev=temp;
        }
        return head;
    }

    Node * delete_in_2DLL(Node * head)
    {
        Node * temp=head;
        while(temp->next!=nullptr)
        {
            temp=temp->next;
        }
        temp->back->next=nullptr;
        temp->back=nullptr;
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
    
};

int main()
{
    Solution sol;
    vector<int> arr={12,5,8,7,4};
    Node* head=sol.convert_arr_2DLL(arr);

    cout<<"Doubly Linked List Initially:"<<endl;

    sol.printList(head);

    head=sol.delete_in_2DLL(head);

    cout<<"Doubly Linked List After Inserting at tail:"<<endl;
    sol.printList(head);

    return 0;


}