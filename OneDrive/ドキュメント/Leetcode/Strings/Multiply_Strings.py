### 43. Multiply Strings
- **Difficulty:** Medium
- **Approach:** Simulated grade-school multiplication using an array of size `m + n` to store intermediate results and carries.
- **Time Complexity:** O(m × n)
- **Space Complexity:** O(m + n)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])

                p1 = i + j
                p2 = i + j + 1

                total = mul + result[p2]

                result[p2] = total % 10
                result[p1] += total // 10

        # Convert array to string and remove leading zeros
        answer = ''.join(map(str, result)).lstrip('0')

        return answer
