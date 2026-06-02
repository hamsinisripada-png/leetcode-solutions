class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])

                # i instead of i + 1 because we can reuse the same number
                backtrack(i, path, remaining - candidates[i])

                path.pop()

        backtrack(0, [], target)
        return result


"""
LeetCode 39 - Combination Sum
Difficulty: Medium

Approach:
- Use Backtracking (Depth-First Search) to generate all possible combinations.
- Start from a candidate and keep adding numbers to the current combination.
- If the remaining target becomes 0, a valid combination is found.
- If the remaining target becomes negative, stop exploring that path.
- Since a number can be used multiple times, the recursive call uses the
  same index (i) instead of moving to the next index.
- Backtracking removes the last added number and explores other possibilities.

Time Complexity:
- O(N^(T/M)) in the worst case
    N = number of candidates
    T = target value
    M = smallest candidate value

Space Complexity:
- O(T/M) for the recursion stack (excluding output storage).
"""
