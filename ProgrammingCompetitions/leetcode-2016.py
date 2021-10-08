# My solution to this problem: https://leetcode.com/problems/maximum-difference-between-increasing-elements/
# To be run with contest driverf

class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxDiff = -1
        for i in range(len(nums)):
            for n in nums[i+1:]:
                if n - nums[i] > maxDiff and n - nums[i] != 0:
                    maxDiff = n - nums[i]
        return maxDiff