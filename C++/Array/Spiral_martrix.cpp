#include<bits/stdc++.h>
using namespace std;

class Solution
{
    vector<int> spiral_matrix(vector<vector<int>> & arr)
    {
        vector<int>ans;
        int top=0;
        int left=0;
        int bottom=arr.size()-1;
        int right=arr[0].size()-1;

        while(top<=bottom && left<=right)
        {
            for(int i=left;i<=right;i++)
            {
                ans.push_back(arr[top][i]);
            }
            top++;
            for(int i=top;i<=bottom;i++)
            {
                ans.push_back(arr[i][right]);
            }
            right--;

            if(top<=bottom)
            {
                for(int i=right;i>=left;i--)
                {
                ans.push_back(arr[bottom][i]);
                }
                bottom--;
            }

            if(left<=right)
            {
                for(int i=bottom;i>=top;i--)
                {
                ans.push_back(arr[i][left]);
                }
                left++;
            }
            
        }
        return ans;
    }
};

int main()
{
    vector<vector<int>> arr={{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}}
    Solution sol;
    vector<int> ans=sol.spiral_matrix(arr);
    for(int x:ans)
    {
        cout<<x<<" ";
    }
    return 0;
}