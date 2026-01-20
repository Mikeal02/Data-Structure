import math
from sys import maxsize
class Solution:
    
    def max_subarray_sum(self,arr):
        n=len(arr)
        max_sum=-math.inf
        for x in arr:
            current_sum=0
            for y in arr:
                current_sum+=y
                max_sum=max(max_sum,current_sum)
           
        
        return max_sum
                
    # Optimal approach: O(n) [kadane's Algo]
    def max_subarray_sum(self,arr):
        n=len(arr)
        max_sum=-math.inf
        current_sum=0
        for x in arr:
            current_sum+=x
            if current_sum<0:
                current_sum=0
            
            max_sum=max(max_sum,current_sum)

        return max_sum

    # Follow Up Question: Print max_subarray
    def max_subarray_sum(self,arr):
        n=len(arr)
        max_sum=-math.inf
        current_sum=0
        start=0
        ansstart,ansend=-1,-1
        for i in range(n):

            if current_sum==0:
                start=i


            if current_sum<0:
                current_sum=0
            
            current_sum+=arr[i]
            if current_sum>max_sum:
                max_sum=current_sum
                ansstart=start
                ansend=i
        
        print("[")
        for i in range(ansstart,ansend+1):
            print(arr[i])
        print("]")

        return max_sum



if __name__=="__main__":
    arr=[2,3,5,-2,8,-4]
    sol=Solution()
    ans=sol.max_subarray_sum(arr)
    print(f"The maximum subarray sum is {ans}")