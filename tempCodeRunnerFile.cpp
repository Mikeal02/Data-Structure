#include<iostream>
#include<vector>
#include<map>
using namespace std;
class Solution
{
    public:
    bool two_sum(vector<int>& arr, int target)
    {
        map<int,int> mp;
        int n=arr.size();
        for(int i=0;i<n;i++)
        {
            int compliment=target-arr[i];
            if(mp.find(compliment)!=mp.end())
            {
                return true;
            }
            mp[arr[i]]=i;
        }
        return false;
    }
};
int main()
{
    vector<int>arr ={2,6,5,8,11};
    Solution sol;
    cout<<sol.two_sum(arr,41);
    return 0;
}