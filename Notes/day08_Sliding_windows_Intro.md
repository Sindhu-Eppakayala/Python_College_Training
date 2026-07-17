# Day 8 – Sliding Window Technique (Introduction)

## Topics Covered
- Sliding window technique for arrays/lists
- Why sliding window is more efficient than naive approaches
- Basic sliding window problems

## Key Notes
- Sliding window is used to solve problems on subarrays/substrings efficiently.
- Instead of recomputing sums or conditions for every position, we "slide" the window:
  - Add new element.
  - Remove old element.
- Common use cases:
  - Maximum/minimum sum of subarray of size `k`.
  - Counting elements within a window.
- Typical time complexity: O(n) instead of O(n*k) for naive approach.

## Example Concepts / Pseudo-Code
- Finding maximum sum of a subarray of length `k` in an array:
  - Compute sum of first window.
  - For each next position, subtract outgoing element and add incoming element.
- Checking number of vowels in sliding window in a string.

## What I Practiced
- Implementing basic sliding window logic for arrays.
- Understanding how start and end pointers move.
- Comparing naive and optimized solutions.

## Reflection
- Sliding window is powerful for many array and string problems.
- I need more practice with different variations (fixed-size and variable-size windows).
- This technique will be useful in algorithms and possibly in log analysis tasks.
