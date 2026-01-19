class Solution:
    # brute force approach: O(2n),O(n)
    def move_zero_to_end(self,arr):
        temp=[]
        for i in range(len(arr)):
            if arr[i]!=0:
                temp.append(arr[i])

        zeros=len(arr)-len(temp)
        temp.extend([0]*zeros)


        for i in range(len(arr)):
            arr[i]=temp[i]

        return arr
        
    # Optimal Approach:O(n)
     def move_zero_to_end(self,arr):
        for i in range(len(arr)):
            if arr[i]==0:
                j=i
                break

        for i in range(j+1,len(arr)):
            if arr[i]!=0:
                arr[i],arr[j]=arr[j],arr[i]
                j+=1
        
        return arr

if __name__=="__main__":
    arr=[1,0,23,2,0,0,4,5,1]
    sol=Solution()
    sol.move_zero_to_end(arr)
    print(arr)
