#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    // Better approach 2: O((m+n)log(m+n)), O(m+n) [Using map]
    vector<int> union_array(vector<int>& arr1, vector<int> &arr2, int n, int m)
    {
        map<int,int> mp;
        vector<int> ans;
        
        for(int i=0;i<n;i++)
        {
            mp[arr1[i]]++;
        }

        for(int i=0;i<m;i++)
        {
            mp[arr2[i]]++;
        }

        for(auto x:mp)
        {
            ans.push_back(x.first);
        }
        return ans;
    }

    

    // Better approach 2: O((m+n)log(m+n)),O(m+n) [Using set]
    vector<int> union_array(vector<int>& arr1, vector<int> &arr2, int n, int m)
    {
        set<int> st;
        vector<int>ans;
        for(int i=0;i<n;i++)
        {
            st.insert(arr1[i]);
        }

        for(int i=0;i<m;i++)
        {
            st.insert(arr2[i]);
        }

        for(int x:st)
        {
            ans.push_back(x);
        }
        return ans;
        
    }

    // Optimal Solution: O(n+m),O(n+m)
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