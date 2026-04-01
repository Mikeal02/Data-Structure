#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    // O(n^2)
    int max_product_subarray(vector<int>&arr)
    {
        int n=arr.size();
        int max_product=arr[0];
        for(int i=0;i<n;i++)
        {
            int current_prod=1;
            for(int j=i;j<n;j++)
            {
                current_prod*=arr[j];
                max_product=max(max_product,current_prod);
            }
        }
        return max_product;
    }

     int max_product_subarray(vector<int>&arr)
     {
        int current_max=arr[0];
        int current_min=arr[0];
        int res=arr[0];
        int n=arr.size();
        int current_prod=1;
        for(int i=1;i<n;i++)
        {
            if(arr[i]<0)
            swap(current_max,current_min);
            current_prod*=arr[i];
            current_max=max(arr[i],current_max*arr[i]);
            current_min=min(arr[i],current_min*arr[i]);

            res=max(res,current_max);

        }
        return res;
     }

};

int main()
{
    vector<int> arr={1,2,-3,0,-4,-5};
    Solution sol;
    int ans=sol.max_product_subarray(arr);
    cout<<ans;
    return 0;
}

