# links:https://leetcode.com/problems/two-sum/description/
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 给定一个无序的数组以及一个元素target，返回等于该元素target的两个元素的下标，注意同一个元素不能使用两次

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        value_map = {}
        for index in range(len(nums)):
            value_map[nums[index]] = index
        for index in range(len(nums)):
            temp_target = target - nums[index]
            if temp_target in value_map and value_map[temp_target] != index:
                return [index, value_map[temp_target]]



if __name__ == '__main__':
    s = Solution()
    r = s.twoSum([2, 7, 11, 11], 13)
    print(r)
