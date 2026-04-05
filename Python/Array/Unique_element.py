"""
DATE: April 5, 2026
PATTERN: XOR, Hashing

APPROACHES:
1. BRUTE FORCE:
- Step 1: Count occurrences of each value with nested loops.
- TIME: O(n^2) | SPACE: O(1)

2. BETTER:
- Step 1: Hash map frequencies; return key with count 1.
- TIME: O(n) | SPACE: O(n)

3. OPTIMAL:
- Step 1: XOR all elements—pairs cancel, singleton remains.
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: x^x=0 and XOR is associative—duplicates disappear, odd one out remains.
"""

# Problem Statement: Given a non empty array of integers arr, every element appears twice except for one. Find that single one 

class solution:
    # Brute force:O(n*n) [we count every element in the array and return the one with count 1]
    def unique_num(self,arr):
        for i in arr:
            for j in arr:
                count=0
                if i==j:
                    count+=1
                if count==1:
                    return i

    # Better solution:O(n),O(n)  [we will use hashmap]
    def unique_num(self,arr):
        hashmap={}
        for i in arr:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        
        for i in hashmap:
            if hashmap[i]==1:
                return i

    # Optimal 1:O(n) [we use xor property x^x=0]
    def unique_num(self,arr):
        ans=0
        for i in arr:
            ans^=i
        return ans





if __name__=="__main__":
    arr=list((4,1,2,1,2,4,3,11,5,3,5))
    sol=solution()
    
    print(f"The unique number is {sol.unique_num(arr)}")