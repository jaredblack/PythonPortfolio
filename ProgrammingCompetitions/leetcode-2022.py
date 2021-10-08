# My solution to this problem: https://leetcode.com/contest/biweekly-contest-62/problems/convert-1d-array-into-2d-array/
# To be run with contest driver

class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        origInd = 0
        arr2d = [[0 for x in range(n)] for y in range(m)]
        if len(original) != m * n:
            return []
        for i in range(m):
            for j in range(n):
                if(origInd < len(original)):
                    arr2d[i][j] = original[origInd]
                else:
                    break
                origInd += 1
        return(arr2d)
    