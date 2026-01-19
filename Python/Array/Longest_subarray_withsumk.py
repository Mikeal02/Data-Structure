class Solution:
    # Brute Force approach: O(n^2)
    # def longest_subarray_k(self,arr,k):
    #     n=len(arr)
    #     max_length=0
    #     for i in range(len(arr)):
    #         sum=0
    #         for j in range(i,len(arr)):
    #             sum+=arr[j]
            
    #             if sum==k:
    #                 max_length=max(max_length,j-i+1)

    #     return max_length
    
    # // Optimal Approach: O(n) [Using SLiding window Algorithm]
     def longest_subarray_k(self,arr,k):
        n=len(arr)
        current_sum=arr[0]
        left,right=0,0
        max_length=0
        while right<n:
            while left<=right and current_sum>k:
                current_sum-=arr[left]
                left+=1

            if current_sum==k:
                max_length=max(max_length,right-left+1)
            right+=1

            if right<n:
                current_sum+=arr[right]

        return max_length
    

if __name__=="__main__":
    arr=[10,5,2,7,1,9]
    sol=Solution()
    k=14
    ans=sol.longest_subarray_k(arr,k)
    print(f"The Longest subarray with sum {k} is {ans}")