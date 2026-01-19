#include<bits/stdc++.h>
using namespace std;
class solution
{
    public:
    // Brute Force Solution: O(n),O(n)[Cause we used set to store elements]
    // vector<int> remove_dup(vector<int> & arr)
    // {
    //     set<int> st;
    //     for(int x:arr)
    //     {
    //         st.insert(x);

    //     }
    //     vector<int> ans(st.begin(),st.end());
    //     return ans;
    // }

    // Optimal Solution:O(n)
    int remove_dup(vector<int>& arr)
    {
        if(arr.empty())return 0;
        int n=arr.size();
        int i=0;
        for(int j=1;j<n;j++)
        {
            if(arr[i]!=arr[j])
            {
                i++;
                arr[i]=arr[j];
            }
        }
        return i+1;
    }
};
int main()
{
    vector<int> arr={1,1,2,2,2,3,3};
    solution sol;
    int ans=sol.remove_dup(arr);
    cout<<ans;
}