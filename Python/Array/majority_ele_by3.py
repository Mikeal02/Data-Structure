from collections import defaultdict


class Solution:
    # Brute force Approach: O(N^2)
    def majority_ele_by3(self,arr):
        n=len(arr)
        for i in range(n):
            count=0
            for j in range(n):
                if arr[i]==arr[j]:
                    count+=1

            if count>n//3:
                return arr[i]


    # Better Approach: O(n)
    def majority_ele_by3(self,arr):
        n=len(arr)
        freq=defaultdict(int)
        for i in range(n):
            freq[arr[i]]+=1

        for x,y in freq.items():
            if y>n//3:
                return x

    # optimal Approach: O(N)
    def majority_ele_by3(self,arr):
        n=len(arr)
        count1=0
        count2=0
        element_1=float("-inf")
        element_2=float("-inf")

        for x in arr:
            if count1==0 and element_2 !=x:
                count1+=1 
                element_1=x

            if count2==0 and element_1 !=x:
                count2+=1 
                element_2=x
                

            elif element_1==x:
                count1+=1

            elif element_2==x:
                count2+=1

            else:
                count1-=1
                count2-=1

        count1,count2=0,0
        if x in arr:
            if x==element_1:
                count1+=1

            if x==element_2:
                count2+=1

        if count1>n//3:
            return element_1

        if count2>n//3:
            return element_2
        


if __name__=="__main__":
    arr=[1,0,0,1,7,1,2,1,1]
    sol=Solution()
    ans=sol.majority_ele_by3(arr)
    print(f"The majority element with occurence greater than N/3 is {ans}")