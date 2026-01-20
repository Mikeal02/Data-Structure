#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
    vector<int> leader_in_array(vector<int>& arr)
    {
        int n=arr.size();
        vector<int> ans;
        for(int i=0;i<n-1;i++)
        {
            bool leader=true;
            for(int j=i+1;j<n;j++)
            {
                if(arr[j]>arr[i])
                {
                    leader=false;
                    break;
                }
            }
            if(leader)ans.push_back(arr[i]);

        }
        ans.push_back(arr[n-1]);
    }

};
int main()
{
    vector<int> arr={10,22,12,3,0,6};
    Solution sol;
    vector<int> ans=sol.leader_in_array(arr);
    cout<<"The maximum subarray sum is:"<<endl;
    for(int x:ans)
    {
        cout<<x<<" ";
    }
    return 0;
}