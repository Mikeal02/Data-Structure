class Solution:

    # def two_sum(self,arr,target):
    #     n=len(arr)
    #     for i in range(n):
    #         for j in range(i+1,n):
    #             current_sum=arr[i]+arr[j]
    #             if current_sum==target:
    #                 return i,j
                
    #     return -1,-1

    # def two_sum(self,arr,target):
    #     freq={}
    #     n=len(arr)
    #     for i in range(n):
    #         remaining=target-arr[i]
    #         if remaining in freq:
    #             return i,freq[remaining]
            
    #         elif remaining not in freq:
    #             freq[arr[i]]=i
    #     return -1,-1
    
    # Optimal Approach: O(nlogn)
    def two_sum(self,arr,target):
        n=len(arr)
        left,right=0,n-1
        arr.sort()
        while left<right:
            current_sum=arr[left]+arr[right]
            if current_sum<target:
                left+=1
            elif current_sum==target:
                return left,right
            
            else:
                right-=1
        return -1,-1


if __name__=="__main__":
    arr=[2,6,5,8,11]
    sol=Solution()
    ans,ans2=sol.two_sum(arr,17)
    print(ans,ans2)