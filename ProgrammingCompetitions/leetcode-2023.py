# My solution to this problem: https://leetcode.com/contest/biweekly-contest-62/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/ 
# To be run with contest driver

class Solution(object):
    def numOfPairs(self, nums, target):
        """
        :type nums: List[str]
        :type target: str
        :rtype: int
        """
        numPairs = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    numPairs += 1
        return numPairs
        