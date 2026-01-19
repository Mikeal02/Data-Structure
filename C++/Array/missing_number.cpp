#include<bits/stdc++.h>
using namespace std;
class solution
{
    public:
    // Brute Force: O(N^2)
    int search(vector<int>& arr,int s)
    {
        for(int i=0;i<arr.size();i++)
        {
            if(arr[i]==s)
            {
                return true;
            }
        }
        return false;
    }
    int missing_num(vector<int>& arr,int N)
    {
        for(int i=1;i<=N;i++)
        {
            if(!search(arr,i))
            {
                return i;
            }
           
        }
        return -1;
    }



    // Optimal 1: O(n),O(1)
    
    int missing_num(vector<int> & arr,int N)
    {
        int n=arr.size();
        int sum=0;
        int sum2=(N*(N+1))/2;
        for(int i=0;i<n;i++)
        {
            sum+=arr[i];
        }
        return sum2-sum1;
    }

    // optimal 2:O(n+N)
    int missing_num(vector<int> & arr,int N)
    {
        int xor1=0;
        int xor2=0;
        for(int i=0;i<arr.size();i++)
        {
            xor1^=arr[i];
        }
        for(int i=1;i<=N;i++)
        {
            xor2^=i;
        }
        return xor1^xor2;
    }

};

int main()
{
    solution sol;
    vector<int> arr={1,2,3,5,6};
    int N;
    cin>>N;
    cout<<"The missing number is "<<sol.missing_num(arr,N);
    return 0;
}