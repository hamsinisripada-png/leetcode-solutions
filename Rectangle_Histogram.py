class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0

        for i in range(len(heights) + 1):
            current_height = 0 if i == len(heights) else heights[i]

            while stack and heights[stack[-1]] > current_height:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)

            stack.append(i)

        return max_area
