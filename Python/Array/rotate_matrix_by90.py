"""
DATE: April 5, 2026
PATTERN: Matrix Transform (Transpose + Reverse)

APPROACHES:
1. BRUTE FORCE:
- Step 1: Copy into new matrix with rotated coordinates.
- TIME: O(n^2) | SPACE: O(n^2)

2. BETTER:
- Step 1: Rotate layer by layer with four-way swaps.
- TIME: O(n^2) | SPACE: O(1)

3. OPTIMAL:
- Step 1: Transpose then reverse each row (90° clockwise for square matrices).
- TIME: O(n^2) | SPACE: O(1)

AHA-MOMENT: 90° rotation factorizes into transpose (flip diagonal) and horizontal flip.
"""

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