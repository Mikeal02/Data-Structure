#include<bits/stdc++h>
using namespace std;

class Solution
{
    public:
    // Brute Force Approach: O(n^2)
    int majority_element(vector<int> &arr)
    {
        int n=arr.size();
        int majority=n/2;
        for(int i=0;i<n;i++)
        {
            int count=0;
            for(int j=0;j<n;j++)
            {
                if(arr[i]==arr[j])
                count++;
            }
            if(count>majority)
            {
                return arr[i];
            }
        }
        return -1;
    }
      // Better Approach:O(n),O(n) [Using hashmap]
    int majority_element(vector<int> &arr)
    {
        int n=arr.size();
        unordered_map<int,int> freq;
        for(int x:arr)
        {
            freq[x]++;
        }
        for(auto x:freq)
        {
            if(x.second>n/2)return x.first;
        }
        return -1;
    }
    
    int majority_element(vector<int> &arr)
    {
        int n=arr.size();
        int ele;
        int count=0;
        for(int i=0;i<n;i++)
        {
            if(count==0)
            {
                count++;
                ele=arr[i];
            }
            else if(ele==arr[i])
            {
                count++;
            }
            else count--;
        }
        
        int count1=0;
        for(int x:arr)
        {
            if(x==ele)count1++;
        }

        if(count1>(n/2))return ele;
        else return -1;
};
int main()
{
    vector<int>arr={7,0,0,1,7,7,2,7,7};
    Solution sol;
    int ans=sol.majority_element(arr);
    cout<<"The majority element with occurence greater than N/2 is "<<ans;
    return 0;
}