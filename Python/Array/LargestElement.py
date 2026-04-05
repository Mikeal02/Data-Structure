"""
DATE: April 5, 2026
PATTERN: Linear Scan / Selection

APPROACHES:
1. BRUTE FORCE:
- Step 1: Compare each element with all others to confirm it is maximum.
- TIME: O(n^2) | SPACE: O(1)

2. BETTER:
- Step 1: Sort and take last element.
- TIME: O(n log n) | SPACE: O(1) to O(n)

3. OPTIMAL:
- Step 1: One pass tracking running maximum.
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: A single sweep suffices—max is an associative fold over the array.
"""

# // brute force solution: O(nlogn)
def maxelement(arr):
    arr.sort()
    return arr[len(arr)-1]

# Optimal solution:O(n)
def maxelement(arr):
    n=len(arr)
    maxi=arr[0]
    for i in range(len(arr)):
        if arr[i]>maxi:
            maxi=arr[i]

    return maxi

if __name__ =="__main__":
    arr=[2,3,4,5,22,65,23,12,53,65,75]
    largest=maxelement(arr)
    print(f"The largest element is {largest}")