/*
 * DATE: April 5, 2026
 * PATTERN: Hashing, Bit Manipulation (XOR)
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: For each element, count frequency with inner loop.
 * - Step 2: Return element with count 1.
 * - TIME: O(n^2) | SPACE: O(1)
 *
 * 2. BETTER:
 * - Step 1: Hash map count occurrences; return key with value 1.
 * - TIME: O(n) | SPACE: O(n) due to map
 *
 * 3. OPTIMAL (if every element appears twice except one):
 * - Step 1: XOR of all numbers—pairs cancel (x^x=0), singleton remains.
 * - TIME: O(n) | SPACE: O(1)
 *
 * AHA-MOMENT: XOR is associative/commutative and self-inverse—duplicates vanish, unique bit pattern survives.
 */

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