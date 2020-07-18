# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# https://leetcode.com/problems/two-sum/description/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}
        for index in range(0, len(nums)):
            num = nums[index]
            if num in comps:
                return [comps[num], index]
            else:
                comps[target-num] = index
        return None


if __name__ == "__main__":
    sol = Solution()
    res = sol.twoSum([2, 11, 7, 15], 22)
    print(res)
