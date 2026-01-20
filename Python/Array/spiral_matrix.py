class Solution:
    def spiral_matrix(self,arr):
        ans=[]
        top,left=0,0
        bottom=len(arr)-1
        right=len(arr[0])-1

        while top<=bottom and left<=right:
            for i in range(left,right+1):
                ans.append(arr[top][i])
            top+=1

            for i in range(top,bottom+1):
                ans.append(arr[i][right])
            right-=1

            if top<=bottom:
                for i in range(right,left-1,-1):
                    ans.append(arr[bottom][i])
                bottom-=1
            
            if left<=right:
                for i in range(bottom,top-1,-1):
                    ans.append(arr[i][left])
                left+=1
        
        return ans

if __name__=="__main__":
    arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    sol=Solution()
    ans=sol.spiral_matrix(arr)

    print(ans)
            