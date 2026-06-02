"""
LeetCode 42 - Trapping Rain Water
Difficulty: Hard

Approach:
- Use the Two Pointer technique.
- Maintain two pointers: left and right.
- Track the maximum height seen so far from both sides:
    - left_max
    - right_max
- Water trapped at a position depends on the smaller of the two maximum heights.
- Move the pointer with the smaller height because the trapped water on that side
  is limited by its current maximum.

Example:
height = [4,2,0,3,2,5]

Water trapped:
index 1 -> 2 units
index 2 -> 4 units
index 3 -> 1 unit
index 4 -> 2 units

Total = 9

Time Complexity:
- O(n)
  Each element is processed at most once.

Space Complexity:
- O(1)
  Only a few extra variables are used.
"""

class Solution:
    def trap(self, height):
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        water = 0

        while left < right:

            # Process the side with smaller height
            if height[left] < height[right]:

                # Update maximum height on the left
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # Water trapped at current position
                    water += left_max - height[left]

                left += 1

            else:

                # Update maximum height on the right
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    # Water trapped at current position
                    water += right_max - height[right]

                right -= 1

        return water