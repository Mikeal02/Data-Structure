/*
 * DATE: April 5, 2026
 * PATTERN: Dynamic Programming (linear recurrence), Fibonacci variant
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Recursively try taking 1 or 2 steps from each position.
 * - TIME: O(2^n) | SPACE: O(n) stack
 *
 * 2. BETTER:
 * - Step 1: dp[i] = dp[i-1] + dp[i-2] with base cases; tabulation array.
 * - TIME: O(n) | SPACE: O(n)
 *
 * 3. OPTIMAL:
 * - Step 1: Rolling two variables: ways to reach i equals sum of ways for i-1 and i-2.
 * - TIME: O(n) | SPACE: O(1)
 *
 * AHA-MOMENT: Number of ways to step n equals Fibonacci(n+1)—same recurrence as 1-2 climb.
 */

