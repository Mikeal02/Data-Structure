"""
DATE: April 5, 2026
PATTERN: Linear Scan, Tournament

APPROACHES:
1. BRUTE FORCE:
- Step 1: Find max, remove all max, find max again.
- TIME: O(n^2) | SPACE: O(n) if copying

2. BETTER:
- Step 1: Sort descending; pick second distinct.
- TIME: O(n log n) | SPACE: O(1) to O(n)

3. OPTIMAL:
- Step 1: Track largest and second largest in one pass.
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: Second place is the best among elements strictly below the current maximum.
"""

arr=[2,3,4,5,22,65,23,12,53,65,75]
# // brute force solution: O(nlogn)
def second_element(arr):
    arr.sort()
    return arr[len(arr)-2]


# Optimal solution:O(n)
def second_element(arr):
    maxi=arr[0]
    maxi2=-1
    for i in range(2,len(arr)):
        if arr[i]>maxi:
            maxi2=maxi
            maxi=arr[i]

        elif arr[i]<maxi and arr[i]>maxi2:
            maxi2=arr[i]

    return maxi2

second_largest=second_element(arr)
print(f"The largest element is {second_largest}")