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

    // Brute Force Solution: O(n+n/2)
    int middle_of_LL(Node* head)
{
    if (head == nullptr) return -1;

    int length = 0;
    Node* temp = head;
    while (temp != nullptr)
    {
        length++;
        temp = temp->next;
    }

    int mid = length / 2;   // second middle for even
    temp = head;
    while (mid--)
        temp = temp->next;

    return temp->val;
}



    // Optimal Approach: O(n/2),O(1) [Using hare and tortoise algorithm]
    int middle_of_LL(Node * head)
    {
        Node * fast=head;
        Node * slow=head;

        while(fast!=nullptr && fast->next!=nullptr)
        {
            slow=slow->next;
            fast=fast->next->next;
        }
        return slow->val;
    }
};

int main()
{
    vector<int> arr={2,3,4,5,6,7,8,9};
    Solution sol;
    Node * head=sol.convert_arr_2LL(arr);

    int ans=sol.middle_of_LL(head);
    cout<<ans;
    return 0;
}