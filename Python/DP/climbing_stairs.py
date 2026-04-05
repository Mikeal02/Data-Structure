"""
DATE: April 5, 2026
PATTERN: Dynamic Programming (Fibonacci recurrence)

APPROACHES:
1. BRUTE FORCE:
- Step 1: DFS counting all 1- or 2-step sequences to top.
- TIME: O(2^n) | SPACE: O(n)

2. BETTER:
- Step 1: dp[i] = dp[i-1] + dp[i-2] tabulated to n.
- TIME: O(n) | SPACE: O(n)

3. OPTIMAL:
- Step 1: Same recurrence with array of size n+1 is already O(n); can compress to two variables if only final count needed.
- TIME: O(n) | SPACE: O(n) here (or O(1) with rolling)

AHA-MOMENT: Ways to reach stair n follows the Fibonacci recurrence—order of 1s and 2s matters combinatorially.
"""

if __name__ == "__main__":
    n=5
    dp=[-1]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-2]+dp[i-1]

    print(dp[n])