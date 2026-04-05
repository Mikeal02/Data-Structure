/*
 * DATE: April 5, 2026
 * PATTERN: Floyd Cycle Detection, Hashing
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: For each node, compare pointer with all previously visited nodes (nested).
 * - TIME: O(n^2) | SPACE: O(1)
 *
 * 2. BETTER:
 * - Step 1: Hash map/set of visited node addresses; repeat means cycle.
 * - TIME: O(n) | SPACE: O(n)
 *
 * 3. OPTIMAL (Floyd):
 * - Step 1: Slow moves 1 step, fast moves 2; if they meet, cycle exists.
 * - TIME: O(n) | SPACE: O(1)
 *
 * AHA-MOMENT: If there is a cycle, the fast pointer trapped inside will eventually lap the slow pointer.
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
    // Brute Force Approach: O(NlogN),O(N)
    bool detect_loop(Node * head)
    {
        unordered_map<Node*, int> visited;
        Node * temp=head;
        while( temp!=nullptr)
        {
            if(visited.find(temp)!=visited.end())
            {
                return true;
            }
            else {
            visited[temp]=1;
            }
            temp=temp->next;
        }
        return false;
    }
    
    // Optimal Approach: O(N)
    bool detect_loop(Node * head)
    {
         if (head == nullptr || head->next == nullptr)
        return false;
        Node * slow=head;
        Node * fast=head;
        while(fast!=nullptr && fast->next!=nullptr)
        {
            slow=slow->next;
            fast=fast->next->next;
            if(slow==fast)
            {
                return true;
            }
            
        }
        return false;
    
    }
};
int main()
{
    Solution sol;
    Node *head= new Node(1);
    head->next= new Node(2);
    head->next->next= new Node(3);
    head->next->next->next= new Node(4);
    head->next->next->next->next= new Node(5);
    // head->next->next->next->next->next=head->next->next;

    cout<<sol.detect_loop(head);
    return 0;
}
