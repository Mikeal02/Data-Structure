"""
DATE: April 5, 2026
PATTERN: Linear Scan / Sliding Window on 1s

APPROACHES:
1. BRUTE FORCE:
- Step 1: For each subarray, count ones.
- TIME: O(n^3) | SPACE: O(1)

2. BETTER:
- Step 1: For each starting 1, extend run forward.
- TIME: O(n^2) worst | SPACE: O(1)

3. OPTIMAL:
- Step 1: One pass; increment streak on 1, reset on 0, track max streak.
- TIME: O(n) | SPACE: O(1)

AHA-MOMENT: Longest block of consecutive 1s is a single-pass streak counter.
"""

# optimal solution: O(n)
def max_ones(arr):
    n=len(arr)
    count=0
    maxones=-1
    for i in range(n):
        if arr[i]==1:
            count=count+1
            maxones=max(maxones,count)

        else:
            count=0
    
    return maxones




if __name__ == "__main__":
    arr=[0,0,1,0,1,1,1,1,0,1,1]
    maxones=max_ones(arr)
    print(f"The maximum consecutive ones are {maxones}")