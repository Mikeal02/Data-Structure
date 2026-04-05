"""
DATE: April 5, 2026
PATTERN: Matrix Boundary Traversal

APPROACHES:
1. BRUTE FORCE:
- Step 1: Simulate movement with visited matrix.
- TIME: O(nm) | SPACE: O(nm)

2. BETTER:
- Step 1: Direction array and step until blocked—still extra state.
- TIME: O(nm) | SPACE: O(nm) visited

3. OPTIMAL:
- Step 1: Maintain top, bottom, left, right; peel layers clockwise until bounds cross.
- TIME: O(nm) | SPACE: O(1) besides output

AHA-MOMENT: Shrink the rectangle after each edge—no visited array needed on a full matrix layer peel.
"""

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
            