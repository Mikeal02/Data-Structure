#include<bits/stdc++.h>
using namespace std;

class solution
{
    public:
    // brute force solution: O(n*n)
    int unique_ele(vector<int>& arr)
    {
        int n=arr.size();
        for(int i=0;i<n;i++)
        {
            int count=0;
            for(int j=0;j<n;j++)
            {
                if(arr[i]==arr[j])
                {
                    count++;
                }
            }
            if(count==1)return i;
        }
        return -1;
    }
    //  better solution: O(n),O(n)[ O(n) cause we used map for storage]
     int unique_ele(vector<int>& arr) {
        unordered_map<int, int> mp;

        for (int x : arr) {
            mp[x]++;
        }

        for (auto x : mp) {
            if (x.second == 1)
                return x.first;
        }
        return -1; // safety
    }

    // optimal solution: O(n)
    int unique_ele(vector<int>& arr)
    {
        int xor1=0;
        for(int i:arr)
        {
            xor1^=i;
        }
        return xor1;
    }
};

int main()
{
    solution sol;
    vector<int> arr={2,3,4,6,4,3,2,6,8};
    cout<<"The unique element is "<<sol.unique_ele(arr);
    return 0;
}