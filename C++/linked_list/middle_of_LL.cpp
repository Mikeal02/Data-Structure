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

    int middle_of_LL(Node * head)
    {
        Node * fast=head;
        Node * slow=head;

        while(fast->next!=nullptr)
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