class Solution:
    # O(N^2)
    def rotate_matrix_by_90(self,arr):
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                arr[i][j],arr[j][i]=arr[j][i],arr[i][j]

        for i in range(n):
            arr[i].reverse()

        return arr
                


                


if __name__=="__main__":
    arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    sol=Solution()
    print(arr)
    ans=sol.rotate_matrix_by_90(arr)

    print(ans)