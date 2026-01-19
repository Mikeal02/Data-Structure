#include<bits/stdc++.h>
using namespace std;

// optimal solution: O(n)
int max_ones(vector<int>& ones)
{
    int len=ones.size();
    int j;
    for(int i=0;i<n;i++)
    {
        if(ones[i]==1)
        {
            j=i;
            break;
        }
    }
    int maxones=-1;
    int count=0;
    for(i=j;i<n;i++)
    {
        if(ones[i]==1)
        {
            count++;
            maxones=max(maxones,count);
        }
        else
        {
            count=0;
        }
    }
    return maxones;
}
int main()
{
    vector<int> ones={0,0,1,0,1,1,1,0,1,1};
    int maxones=max_ones(ones);
    cout<<"The maximum consecutive ones are:"<< maxones;
}