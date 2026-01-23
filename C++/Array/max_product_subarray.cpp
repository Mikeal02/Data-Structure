#include<bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    int max_product_subarray(vector<int>&arr)
    {
        int n=arr.size();
        int max_product=arr[0];
        for(int i=0;i<n;i++)
        {
            current_prod=1;
            for(int j=i;i<n;j++)
            {
                current_prod*=arr[j];
                max_product=max(max_product,current_prod);
            }
        }
        return max_product;
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

