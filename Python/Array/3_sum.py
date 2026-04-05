"""
DATE: April 5, 2026
PATTERN: Brute Enumeration, Sorting + Two Pointers (extension)

APPROACHES:
1. BRUTE FORCE:
- Step 1: Try all triples (i,j,k); check sum zero; dedupe via sorted tuple in a set.
- TIME: O(n^3) | SPACE: O(k) for unique triplets

2. BETTER:
- Step 1: Fix one element, reduce to sorted two-sum on the rest.
- TIME: O(n^2) after sort O(n log n) | SPACE: O(1) to O(n)

3. OPTIMAL:
- Step 1: Sort array; for each i, two pointers lo/hi on i+1..end avoiding duplicate skips.
- TIME: O(n^2) | SPACE: O(1) extra besides output

AHA-MOMENT: After sorting, duplicates are adjacent—skip equal neighbors to avoid duplicate triplets.
"""

class Solution:
    def three_sum(self,arr):
        st=set()
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if arr[i]+arr[j]+arr[k]==0:
                        triplet=tuple(sorted([arr[i],arr[j],arr[k]]))
                        st.add(triplet)

        return [list(triplet) for triplet in st]

if __name__=="__main__":
    arr=[-1,0,1,2,-1,-4]
    sol=Solution()
    result=sol.three_sum(arr)
    for triplet in result:
        print(triplet)



