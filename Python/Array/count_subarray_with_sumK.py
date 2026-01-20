class Solution:
    # def count_subarray_with_sumk(self,arr,target):
    #     n=len(arr)
    #     count=0
        
    #     for i in range(n):
    #         current_sum=0
    #         for j in range(i,n):
    #             current_sum+=arr[j]
    #             if current_sum==target:
    #                 count+=1
                    
    #     return count
                
    def count_subarray_with_sumk(self,arr,target):
        n=len(arr)
        count=0
        freq={}
        freq[0]=1
        current_sum=0
        for i in range(n):
            current_sum+=arr[i]
            remove=current_sum-target
            if (remove) in freq:
                count+=freq[(remove)]

            
            freq[current_sum]=freq.get(current_sum,0)+1
        return count

    

if __name__=="__main__":
    arr=[2,3,1,4]
    sol=Solution()
    k=5
    ans=sol.count_subarray_with_sumk(arr,k)
    print(f"The number of subarray with sum k is {ans}")