# https://leetcode.com/problems/rotate-image/

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]], n: int) -> None:
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        self.transpose(matrix, n)
        for i in range(n):
            matrix[i][:] = matrix[i][::-1]
