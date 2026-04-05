"""
DATE: April 5, 2026
PATTERN: Linear Verification

APPROACHES:
1. BRUTE FORCE:
- Step 1: Check every pair i<j for arr[i]<=arr[j].
- TIME: O(n^2) | SPACE: O(1)

2. BETTER:
- Step 1: Compare arr to sorted(arr) element-wise.
- TIME: O(n log n) | SPACE: O(n) for sorted copy

3. OPTIMAL:
- Step 1: Verify adjacent pairs non-decreasing in one pass.
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: Global sortedness for total order reduces to local adjacent checks.
"""

# Brute Force Solution: O(nlogn)
def is_sort(arr):
    if arr==sorted(arr):
        return True
    else:
        return False

# Optimal Solution: O(n)
def is_sort(arr):
    for i in range(1,len(arr)):
        if arr[i-1]>arr[i]:
            return False
        else :
            continue
    return True

arr=[1,2,3,4,5]
print(is_sort(arr))
    