<a name='top'></a># 📂 IDE-Style DSA Explorer

**Total Problems:** 23 | **🔵 C++:** 0 | **🟡 Python:** 0 | **🏁 CP:** 0

## 📌 Navigation Tree
- **General**
  - [Miscellaneous](#general-miscellaneous)

---

# 🛠️ General

## <a name='general-miscellaneous'></a>📁 General > Miscellaneous

### 🔴 2 Sum
- DATE: April 5, 2026
- PATTERN: Hashing, Two Pointers
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: Try every pair (i, j) and check if arr[i] + arr[j] == target.
- - Step 2: Return YES if any pair works, else NO.
- - TIME: O(n^2) | SPACE: O(1)
-
- 2. BETTER:
- - Step 1: One pass; for each arr[i], need (target - arr[i]) among indices before i.
- - Step 2: Store visited values in an unordered_map for O(1) lookup.
- - TIME: O(n) | SPACE: O(n) due to hash map
-
- 3. OPTIMAL (when array is sorted):
- - Step 1: Sort (or start sorted), place pointers at both ends.
- - Step 2: Move left/right based on whether current sum is below or above target.
- - TIME: O(n log n) if sort needed, else O(n) | SPACE: O(1) for two pointers
- CONFIDENCE: low
- AHA-MOMENT: Complement lookup (target - x) turns pair search into O(n) with a map; two pointers work only when order is sorted.

🔗 [Open Source File](./2_sum.cpp) | [↑ Back to Top](#top)

### 🟡 Count Subarray With Sumk
- DATE: April 5, 2026
- PATTERN: Prefix Sum, Hashing
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: Fix start i, extend j while tracking running sum; increment count when sum equals K.
- - Step 2: Repeat for all i.
- - TIME: O(n^2) | SPACE: O(1)
-
- 2. BETTER:
- - Step 1: Build prefix array; check all (i,j) pairs via prefix difference.
- - TIME: O(n^2) | SPACE: O(n) for prefix array
-
- 3. OPTIMAL:
- - Step 1: Maintain running prefix sum; map freq of each prefix (initialize freq[0]=1).
- - Step 2: For each prefix P, add freq[P - K] to count, then freq[P]++.
- - TIME: O(n) | SPACE: O(n) due to unordered_map
- CONFIDENCE: Medium
- AHA-MOMENT: Subarray sum ending at index j equals K iff prefix[j] - prefix[i-1] = K, i.e. count prior prefixes equal to prefix[j] - K.

🔗 [Open Source File](./count_subarray_with_sumK.cpp) | [↑ Back to Top](#top)

### ⚪ Issort
- DATE: April 5, 2026
- PATTERN: Linear Scan
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: For every i < j, verify arr[i] <= arr[j] (non-decreasing check all pairs).
- - TIME: O(n^2) | SPACE: O(1)
-
- 2. BETTER:
- - Step 1: Sort a copy and compare to original, or compare adjacent after sort of index pairs.
- - TIME: O(n log n) | SPACE: O(n)
-
- 3. OPTIMAL:
- - Step 1: Single pass from index 1; if any arr[i] < arr[i-1], not sorted ascending.
- - TIME: O(n) | SPACE: O(1)
-
- AHA-MOMENT: Non-decreasing order is equivalent to every adjacent pair being valid—no need to compare all pairs.

🔗 [Open Source File](./issort.cpp) | [↑ Back to Top](#top)

### ⚪ Kadane Algo
- DATE: April 5, 2026
- PATTERN: Dynamic Programming (running state), Array
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: Enumerate every subarray (i..j) and compute sum.
- - Step 2: Track global maximum sum.
- - TIME: O(n^3) naive or O(n^2) with running inner sum | SPACE: O(1)
-
- 2. BETTER:
- - Step 1: Prefix sums: max subarray ending at j is max over i of (P[j]-P[i-1]) in O(n^2).
- - TIME: O(n^2) | SPACE: O(n) for prefix array
-
- 3. OPTIMAL (Kadane):
- - Step 1: Track current_sum; reset or extend: if current_sum + arr[i] is best, extend; optionally reset negative running sum to 0 (all-negative arrays need tracking max element separately).
- - Step 2: Update global max each step.
- - TIME: O(n) | SPACE: O(1)
-
- AHA-MOMENT: Optimal subarray ending at i either extends the best ending at i-1 or starts fresh at i—constant state suffices.

🔗 [Open Source File](./kadane_algo.cpp) | [↑ Back to Top](#top)

### ⚪ Largestelement
- DATE: April 5, 2026
- PATTERN: Array Scan / Selection
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: Compare every element with every other to find the maximum (redundant comparisons).
- - TIME: O(n^2) | SPACE: O(1)
-
- 2. BETTER:
- - Step 1: Sort ascending and take last element as maximum.
- - TIME: O(n log n) | SPACE: O(1) to O(n) depending on sort
-
- 3. OPTIMAL:
- - Step 1: One linear scan maintaining running maximum.
- - TIME: O(n) | SPACE: O(1)
-
- AHA-MOMENT: Maximum over a set is computable in one pass—sorting is unnecessary for finding the max alone.

🔗 [Open Source File](./largestElement.cpp) | [↑ Back to Top](#top)

### ⚪ Leader In The Array
- DATE: April 5, 2026
- PATTERN: Array, Greedy / Right-to-left scan
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: For each index i, scan all elements to the right; i is a leader if nothing on the right is greater.
- - TIME: O(n^2) | SPACE: O(n) for answer
-
- 2. BETTER:
- - Step 1: Precompute suffix maximum array so each position checked in O(1).
- - TIME: O(n) | SPACE: O(n) for suffix array
-
- 3. OPTIMAL:
- - Step 1: Traverse from right to left; keep max_seen from the right; element is leader if it exceeds max_seen.
- - Step 2: Last element is always a leader; reverse collected order if original left-to-right order is needed.
- - TIME: O(n) | SPACE: O(1) extra besides output
-
- AHA-MOMENT: Leaders depend only on the maximum of the suffix—carry that max from the end in one pass.

🔗 [Open Source File](./Leader_in_the_array.cpp) | [↑ Back to Top](#top)

### ⚪ Left Rotate By 1
- DATE: April 5, 2026
- PATTERN: Array Rotation
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: Pop front and push to end using extra list operations or repeated single-step shifts.
- - TIME: O(n) per rotation × rotations | SPACE: O(1) for one step
-
- 2. BETTER:
- - Step 1: Copy to new array with shifted indices (i-k mod n).
- - TIME: O(n) | SPACE: O(n)
-
- 3. OPTIMAL (rotate by 1):
- - Step 1: Store first element, shift all elements left by one index, place stored value at end.
- - TIME: O(n) | SPACE: O(1)
-
- AHA-MOMENT: Left rotate by 1 is a single cyclic shift—one temp and one linear move.

🔗 [Open Source File](./Left_rotate_by_1.cpp) | [↑ Back to Top](#top)

### ⚪ Left Rotate By D
- DATE: April 5, 2026
- PATTERN: Array Reversal, Rotation
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: Perform D single left rotations (each O(n)).
- - TIME: O(n * D) | SPACE: O(1)
-
- 2. BETTER:
- - Step 1: Use extra array of size n and place arr[(i+k)%n].
- - TIME: O(n) | SPACE: O(n)
-
- 3. OPTIMAL:
- - Step 1: Reverse [0..k-1], reverse [k..n-1], reverse whole array (adjust for left vs right).
- - TIME: O(n) | SPACE: O(1)
-
- AHA-MOMENT: Rotation is three reversals—brings block moves without extra storage.

🔗 [Open Source File](./left_rotate_by_D.cpp) | [↑ Back to Top](#top)

### ⚪ Longest Sub Array With Sumk
- DATE: April 5, 2026
- PATTERN: Prefix Sum, Hashing, Sliding Window
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: Enumerate all subarrays (i..j) and compute each sum.
- - Step 2: Track maximum length where sum equals K.
- - TIME: O(n^3) with naive resum, or O(n^2) with running sum inner loop | SPACE: O(1)
-
- 2. BETTER:
- - Step 1: Use prefix sums P[j] - P[i-1] to get any subarray sum in O(1) after O(n) prefix build.
- - Step 2: Still need pairs (i,j) without extra structure—often O(n^2).
- - TIME: O(n^2) | SPACE: O(n) for prefix array
-
- 3. OPTIMAL:
- - Step 1 (general integers): For each end index, need earlier prefix equal to (current_prefix - K); track first index of each prefix in a map for longest length.
- - Step 2 (non-negative array only): Sliding window shrink when sum > K.
- - TIME: O(n) | SPACE: O(n) for hash map (window is O(1) extra)
-
- AHA-MOMENT: Longest length with sum K is a “first occurrence of prefix” problem: length = i - firstIndex[prefix - K].

🔗 [Open Source File](./Longest_sub_array_with_sumK.cpp) | [↑ Back to Top](#top)

### ⚪ Majority Element2
- DATE: April 5, 2026
- PATTERN: Hashing, Boyer–Moore Voting
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: For each element, count occurrences with inner loop over full array.
- - Step 2: Return element with count > n/2 if exists.
- - TIME: O(n^2) | SPACE: O(1)
-
- 2. BETTER:
- - Step 1: Frequency map over all elements.
- - Step 2: Find key with value > n/2.
- - TIME: O(n) | SPACE: O(n) due to hash map
-
- 3. OPTIMAL (Boyer–Moore majority vote):
- - Step 1: Cancel pairs of distinct elements; remaining candidate is only possible majority.
- - Step 2: Second pass to verify count > n/2.
- - TIME: O(n) | SPACE: O(1)
-
- AHA-MOMENT: The majority element survives pairwise cancellation; at most one candidate needs verification.

🔗 [Open Source File](./majority_element2.cpp) | [↑ Back to Top](#top)

### ⚪ Majority Ele 2
- DATE: April 5, 2026
- PATTERN: Hashing, Boyer–Moore Voting
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: For each element, count occurrences with inner loop over full array.
- - Step 2: Return element with count > n/2 if exists.
- - TIME: O(n^2) | SPACE: O(1)
-
- 2. BETTER:
- - Step 1: Frequency map over all elements.
- - Step 2: Find key with value > n/2.
- - TIME: O(n) | SPACE: O(n) due to hash map
-
- 3. OPTIMAL (Boyer–Moore majority vote):
- - Step 1: Cancel pairs of distinct elements; remaining candidate is only possible majority.
- - Step 2: Second pass to verify count > n/2.
- - TIME: O(n) | SPACE: O(1)
-
- AHA-MOMENT: The majority element survives pairwise cancellation; at most one candidate needs verification.

🔗 [Open Source File](./Majority_ele_2.cpp) | [↑ Back to Top](#top)

### ⚪ Maxones
- DATE: April 5, 2026
- PATTERN: Sliding Window / Linear Scan
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: For each subarray, count ones and track maximum consecutive block.
- - TIME: O(n^3) or O(n^2) | SPACE: O(1)
-
- 2. BETTER:
- - Step 1: Single pass from each index where arr[i]==1 as start—still redundant.
- - TIME: O(n^2) worst | SPACE: O(1)
-
- 3. OPTIMAL:
- - Step 1: One traversal; extend count while seeing 1, reset on 0, update max streak.
- - TIME: O(n) | SPACE: O(1)
-
- AHA-MOMENT: Longest run of 1s is found by one pass with a running counter reset at zeros.

🔗 [Open Source File](./maxones.cpp) | [↑ Back to Top](#top)

### ⚪ Max Product Subarray
- DATE: April 5, 2026
- PATTERN: Dynamic Programming, Array
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: Enumerate all subarrays and multiply elements; track maximum product.
- - TIME: O(n^2) or O(n^3) | SPACE: O(1)
-
- 2. BETTER:
- - Step 1: Prefix/suffix products with care for zeros—still need sign handling.
- - TIME: O(n^2) naive extensions | SPACE: O(1)
-
- 3. OPTIMAL:
- - Step 1: Track both current maximum and minimum ending here (negatives flip min to max).
- - Step 2: Update answer from current_max each index.
- - TIME: O(n) | SPACE: O(1)
-
- AHA-MOMENT: A negative number turns the smallest subproduct into the largest—track min and max together.

🔗 [Open Source File](./max_product_subarray.cpp) | [↑ Back to Top](#top)

### ⚪ Missing Number
- DATE: April 5, 2026
- PATTERN: Math (sum/XOR), Hashing
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: For each number 1..N, linear search in array for presence.
- - TIME: O(N^2) | SPACE: O(1)
-
- 2. BETTER:
- - Step 1: Use hash set of array elements; scan 1..N for missing.
- - TIME: O(N) | SPACE: O(N)
-
- 3. OPTIMAL:
- - Step 1: Sum formula N(N+1)/2 minus sum(arr), or XOR all indices and values together.
- - TIME: O(N) | SPACE: O(1)
-
- AHA-MOMENT: Expected sum (or XOR) minus actual isolates the single missing number without extra storage.

🔗 [Open Source File](./missing_number.cpp) | [↑ Back to Top](#top)

### ⚪ Move 0To End
- DATE: April 5, 2026
- PATTERN: Two Pointers
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: Build new list of non-zeros in order, append zeros to fill.
- - TIME: O(n) | SPACE: O(n) auxiliary vector
-
- 2. BETTER:
- - Step 1: Stable partition with extra array copy (two passes over copy).
- - TIME: O(n) | SPACE: O(n)
-
- 3. OPTIMAL:
- - Step 1: Slow pointer for next non-zero slot; fast pointer scans; swap non-zeros forward.
- - TIME: O(n) | SPACE: O(1)
-
- AHA-MOMENT: Partition the array in-place: the “write” index only advances when a non-zero is found.

🔗 [Open Source File](./move_0to_end.cpp) | [↑ Back to Top](#top)

### ⚪ Rearrange By Sign
- DATE: April 5, 2026
- PATTERN: Two Pointers, Array Partition
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: Split into positives and negatives lists, then interleave by index rules.
- - TIME: O(n) | SPACE: O(n) for extra vectors
-
- 2. BETTER:
- - Step 1: Single pass to place positives at even and negatives at odd indices using separate write pointers (if counts balanced).
- - TIME: O(n) | SPACE: O(n) for result array
-
- 3. OPTIMAL (structure in code):
- - Step 1: Separate positive/negative buckets then merge in required alternating pattern.
- - TIME: O(n) | SPACE: O(n) for output (in-place alternating with negatives/positives may need follow-up variants).
-
- AHA-MOMENT: Decouple “collect by sign” from “scatter to alternating slots”—two-phase keeps logic simple.

🔗 [Open Source File](./rearrange_by_sign.cpp) | [↑ Back to Top](#top)

### ⚪ Removedupfromsorted
- DATE: April 5, 2026
- PATTERN: Two Pointers, In-place Array
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: Insert elements into a set from sorted array, copy back (or check each against all prior).
- - TIME: O(n log n) for set | SPACE: O(n)
-
- 2. BETTER:
- - Step 1: Use set to collect unique in sorted order, return new length/size.
- - TIME: O(n log n) | SPACE: O(n)
-
- 3. OPTIMAL:
- - Step 1: Slow pointer i at last unique; fast j scans; when arr[j]!=arr[i], advance i and assign arr[i]=arr[j].
- - Step 2: Return i+1 as new length.
- - TIME: O(n) | SPACE: O(1)
-
- AHA-MOMENT: Sorted duplicates are contiguous—one slow pointer “compresses” unique values in place.

🔗 [Open Source File](./RemoveDupFromSorted.cpp) | [↑ Back to Top](#top)

### ⚪ Repeating Missing
- DATE: April 5, 2026
- PATTERN: Hashing / Counting
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: For each number 1..n, count occurrences by scanning the whole array each time.
- - TIME: O(n^2) | SPACE: O(1)
-
- 2. BETTER:
- - Step 1: Frequency map or array of size n+1; increment per value; find value with count 2 and missing 0.
- - TIME: O(n) | SPACE: O(n)
-
- 3. OPTIMAL (math variants exist):
- - Step 1: Use counting array as in “better” when values in 1..n—same asymptotics, minimal overhead.
- - Alternative: sum and sum of squares equations to derive repeating and missing (O(n) time, O(1) space).
- - TIME: O(n) | SPACE: O(n) for frequency array here, or O(1) with algebraic method
-
- AHA-MOMENT: One duplicate and one missing show up as count 2 and count 0 in a 1..n index frequency table.

🔗 [Open Source File](./repeating_missing.cpp) | [↑ Back to Top](#top)

### ⚪ Second Largest
- DATE: April 5, 2026
- PATTERN: Array Scan
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: Find max, then find max among elements strictly less than first max (two passes).
- - Step 2: Or compare all pairs for second largest.
- - TIME: O(n^2) for pair approach | SPACE: O(1)
-
- 2. BETTER:
- - Step 1: Sort descending (or ascending) and take second distinct position.
- - TIME: O(n log n) | SPACE: O(1) to O(n)
-
- 3. OPTIMAL:
- - Step 1: One pass: maintain largest and second_largest; update when seeing larger or smaller-than-max but larger than second.
- - TIME: O(n) | SPACE: O(1)
-
- AHA-MOMENT: Track two leaders in one pass—no sort needed for second place.

🔗 [Open Source File](./Second_largest.cpp) | [↑ Back to Top](#top)

### ⚪ Sort 012
- DATE: April 5, 2026
- PATTERN: Dutch National Flag, Two Pointers
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: Sort the array with generic comparison sort.
- - TIME: O(n log n) | SPACE: O(log n) stack for sort
-
- 2. BETTER:
- - Step 1: Count occurrences of 0, 1, 2; overwrite array in three segments.
- - TIME: O(n) | SPACE: O(1) for counts (two passes)
-
- 3. OPTIMAL (DNF):
- - Step 1: Three pointers low, mid, high; mid drives 0 to left, 2 to right, 1 in middle.
- - TIME: O(n) | SPACE: O(1) single pass
-
- AHA-MOMENT: Only three values—partition by maintaining three regions with mid pointer as the frontier.

🔗 [Open Source File](./Sort_012.cpp) | [↑ Back to Top](#top)

### ⚪ Spiral Martrix
- DATE: April 5, 2026
- PATTERN: Matrix Simulation, Boundary Traversal
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: Mark visited cells and repeatedly pick next clockwise neighbor (complex).
- - TIME: O(n*m) | SPACE: O(n*m) visited
-
- 2. BETTER:
- - Step 1: Layer-by-layer simulation with direction index and turn-on-wall logic.
- - TIME: O(n*m) | SPACE: O(1) extra
-
- 3. OPTIMAL:
- - Step 1: Maintain top, bottom, left, right; spiral left→right, top→bottom, right→left, bottom→top while shrinking bounds.
- - TIME: O(n*m) | SPACE: O(1) besides output
-
- AHA-MOMENT: After each edge, shrink the corresponding boundary—no visited matrix needed when layers don’t overlap.

🔗 [Open Source File](./Spiral_martrix.cpp) | [↑ Back to Top](#top)

### ⚪ Union
- DATE: April 5, 2026
- PATTERN: Hashing, Two Pointers, Sorting
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: Concatenate both arrays into a list and remove duplicates by checking each element against all seen (nested loops).
- - Step 2: Sort the result if order is required.
- - TIME: O((n+m)^2) worst naive dedup | SPACE: O(n+m)
-
- 2. BETTER:
- - Step 1: Insert all elements from both arrays into a set (or map keys) for uniqueness.
- - Step 2: Copy sorted order from set/map into answer vector.
- - TIME: O((n+m) log(n+m)) | SPACE: O(n+m) for the set
-
- 3. OPTIMAL (when both arrays are already sorted):
- - Step 1: Merge-like two pointers, skipping duplicates within each array and across pointers.
- - Step 2: Push smaller head, advance; on equality advance both.
- - TIME: O(n+m) | SPACE: O(1) extra besides output
-
- AHA-MOMENT: Uniqueness is a set problem; sorted inputs unlock linear two-pointer merge without global sort.

🔗 [Open Source File](./Union.cpp) | [↑ Back to Top](#top)

### ⚪ Unique Element
- DATE: April 5, 2026
- PATTERN: Hashing, Bit Manipulation (XOR)
-
- APPROACHES:
- 1. BRUTE FORCE:
- - Step 1: For each element, count frequency with inner loop.
- - Step 2: Return element with count 1.
- - TIME: O(n^2) | SPACE: O(1)
-
- 2. BETTER:
- - Step 1: Hash map count occurrences; return key with value 1.
- - TIME: O(n) | SPACE: O(n) due to map
-
- 3. OPTIMAL (if every element appears twice except one):
- - Step 1: XOR of all numbers—pairs cancel (x^x=0), singleton remains.
- - TIME: O(n) | SPACE: O(1)
-
- AHA-MOMENT: XOR is associative/commutative and self-inverse—duplicates vanish, unique bit pattern survives.

🔗 [Open Source File](./Unique_element.cpp) | [↑ Back to Top](#top)

---
