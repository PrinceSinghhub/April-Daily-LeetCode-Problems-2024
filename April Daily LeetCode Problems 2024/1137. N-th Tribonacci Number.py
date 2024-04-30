from numpy import *
class Solution(object):
    def tribonacci(self, n):

        if n == 0 or n == 1:
            return n

        if n == 2:
            return 1

        Matrix = zeros((n - 2, 4), dtype=int)

        Matrix[0][0] = 0
        Matrix[0][1] = 1
        Matrix[0][2] = 1
        Matrix[0][3] = 2

        for i in range(1, len(Matrix)):

            Sum = 0
            for j in range(4):
                if j == 3:
                    Matrix[i][j] = Sum
                else:
                    Matrix[i][j] = Matrix[i - 1][j + 1]
                    Sum += Matrix[i][j]

        return Matrix[len(Matrix) - 1][len(Matrix[0]) - 1]