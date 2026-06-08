class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for row in matrix:
            row.reverse()


"""Input:

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

After transpose:

[
    [1,4,7],
    [2,5,8],
    [3,6,9]
]

After reversing rows:

[
    [7,4,1],
    [8,5,2],
    [9,6,3]  """
