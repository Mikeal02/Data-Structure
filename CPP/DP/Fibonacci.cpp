/*
 * DATE: April 5, 2026
 * PATTERN: Dynamic Programming (Fibonacci), Space Optimization
 *
 * APPROACHES:
 * 1. BRUTE FORCE:
 * - Step 1: Recursive F(n)=F(n-1)+F(n-2) without memo; recomputes subproblems exponentially.
 * - TIME: O(2^n) | SPACE: O(n) call stack
 *
 * 2. BETTER:
 * - Step 1: Top-down memoization or bottom-up dp array of size n+1.
 * - TIME: O(n) | SPACE: O(n)
 *
 * 3. OPTIMAL:
 * - Step 1: Keep only last two values (prev2, prev) and iterate from 2 to n.
 * - TIME: O(n) | SPACE: O(1)
 *
 * AHA-MOMENT: F(n) depends only on F(n-1) and F(n-2)—the full table is unnecessary.
 */

