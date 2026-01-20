class Solution:
    # Brute force approach: O(n^2)
    def leader_in_array(self,arr):
        n=len(arr)
        ans=[]
        for i in range(len(n)-1):
            leader=True
            for j in range(i+1,len(n)):
                if arr[j]>arr[i]:
                    leader=False
                    break
            
            if leader==True:
                ans.append(arr[i])

        ans.append(arr[n-1])
        return ans

                



    # Optimal Approach: O(n)
    def leader_in_array(self,arr):
        n=len(arr)
        ans=[]
        max_element=arr[-1]
        ans.append(arr[-1])
        for i in range(n-2,-1,-1):
            if arr[i]>max_element:
                ans.append(arr[i])
                max_element=arr[i]

        ans.reverse()
        return ans

if __name__=="__main__":
    arr=[10,22,12,3,0,6]
    sol=Solution()
    ans=sol.leader_in_array(arr)
    print(ans)
