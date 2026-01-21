#include<bits//stdc++.h>
using namespace std;

class Solution 
{
    public:
    // brute force approach: O(2n)
    void sort_012(vector<int> & arr)
    {
        int n=arr.size();
        int count_zero=0,count_one=0, count_two=0;
        for(int i=0;i<n;i++)
        {
            if(arr[i]==0)count_zero++;
            else if(arr[i]==1)count_one++;
            else count_two++;
        }
        int index=0;
        while(count_zero>0)
        {
            arr[index++]=0;
            count_zero--;
        }
        
        while(count_one>0)
        {
            arr[index++]=1;
            count_one--;
        }
        while(count_two>0)
        {
            arr[index++]=2;
            count_two--;
        }

    }
    // Optimal Approach:O(n)
    void sort_012(vector<int> & arr)
    {
        int n=arr.size();
        int low=0,mid=0;
        int high=n-1;
        while(mid<=hgh)
        {
            if(arr[mid]==0)
            {
                swap(arr[low],arr[mid]);
                low++;
                mid++;
            }
            else if(arr[mid]==1)
            {
                mid++;
            }
            else
            {
                swap(arr[mid],arr[high]);
                high--;
            }
        }
    }
};

int main()
{
    vector<int> arr={1,0,2,1,0};
    Solution sol;
    sol.sort_012(arr);
    for(int x:arr)
    {
        cout<<x<<" ";
    }
    return 0;
}