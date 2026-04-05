"""
DATE: April 5, 2026
PATTERN: Two Pointers on Sorted Array

APPROACHES:
1. BRUTE FORCE:
- Step 1: Build set from array elements.
- TIME: O(n log n) for sorted set ops | SPACE: O(n)

2. BETTER:
- Step 1: New list with unique via scan of sorted input.
- TIME: O(n) | SPACE: O(n)

3. OPTIMAL:
- Step 1: Slow pointer for last unique index; fast scans; overwrite in place.
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: Sorted duplicates sit together—one writer index suffices.
"""

# Brute Force Solution: O(1), O(n)
def remove_dup(arr):
    arr2=set(arr)
    return len(arr2)

# Optimal Solution: O(n)
def remove_dup(arr):
    if len(arr)==0:
        return 0
    i=0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
        
    return i+1


arr=[1,1,2,2,2,3,3]
ans=remove_dup(arr)
print(ans)