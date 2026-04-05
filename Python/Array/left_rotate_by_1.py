"""
DATE: April 5, 2026
PATTERN: Array Rotation

APPROACHES:
1. BRUTE FORCE:
- Step 1: Pop index 0 and append repeatedly using list operations.
- TIME: O(n) per step | SPACE: O(n) if slicing

2. BETTER:
- Step 1: New array with indices shifted by one mod n.
- TIME: O(n) | SPACE: O(n)

3. OPTIMAL:
- Step 1: Save first, shift left in place, write saved at end.
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: One cyclic left shift is a single pass with one temp variable.
"""

class solution:
    # optimal solution: O(n),O(1)
    def left_rotate(self,arr):
        first_element=arr[0]
        for i in range(1,len(arr)):
            arr[i-1]=arr[i]
        arr[-1]=first_element


if __name__ == "__main__":
    sol=solution()
    arr=list(range(1,9))
    sol.left_rotate(arr)
    print(arr)

