#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    vector<int> union_array(vector<int>& arr1, vector<int> &arr2, int n, int m)
    {
        int i=0;
        int j=0;
        vector<int> ans;
        while(i<n && j<m)
        {
            if(arr1[i]==arr2[j])
            {
                if(ans.empty()|| ans.back()!=arr1[i])
                {
                    ans.push_back(arr1[i]);
                }
                i++;
                j++;
            }

            else if(arr1[i]<arr2[j])
            {
                if(ans.empty()|| ans.back()!=arr1[i])
                {
                    ans.push_back(arr1[i]);
                }
                i++;
                
            }
            else{
                 if(ans.empty()|| ans.back()!=arr2[j]){
                        ans.push_back(arr2[j]);
                 }
                 j++;
            }
        }
        while(i<n)
        {
             if(ans.empty()|| ans.back()!=arr1[i])
            {
                ans.push_back(arr1[i]);
            }
            i++;
        }

        while(j<m)
        {
             if(ans.empty()|| ans.back()!=arr2[j])
            ans.push_back(arr2[j]);
            j++;
        }

        return ans;
    }
};

int main()
{
    Solution sol;
    vector<int> arr1={1,2,3,4,5};
    vector<int> arr2={2,3,4,4,5};
    vector<int> ans;
    ans=sol.union_array(arr1,arr2,arr1.size(),arr2.size());
    for(int x:ans)
    {
        cout<<x<<" ";
    }
    return 0;
}