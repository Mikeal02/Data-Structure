"""
DATE: April 5, 2026
PATTERN: Reversal Rotation

APPROACHES:
1. BRUTE FORCE:
- Step 1: Rotate left by one, D times.
- TIME: O(n * D) | SPACE: O(1)

2. BETTER:
- Step 1: Extra array with index (i - D) mod n.
- TIME: O(n) | SPACE: O(n)

3. OPTIMAL:
- Step 1: Reverse first k, reverse rest, reverse whole (adjust for left/right).
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: Three reversals implement rotation without extra storage.
"""

class solution:
    # optimal solution: O(n),O(1)

    def reverse(self,arr,start,end):
        while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1

    def left_rotate_by_D(self,arr,k,direction):
        n=len(arr)
        k%=n
        if n==0 or k==0:
            return
        
        if direction=="left":
            self.reverse(arr,0,k-1)
            self.reverse(arr,k,n-1)
            self.reverse(arr,0,n-1)
        else:
            self.reverse(arr,0,n-1)
            self.reverse(arr,0,k-1)
            self.reverse(arr,k,n-1)
            
if __name__ == "__main__":
    sol=solution()
    n=int(input())
    dir=input()
    arr=list(range(1,9))
    sol.left_rotate_by_D(arr,n,dir)
    print(arr)
   
