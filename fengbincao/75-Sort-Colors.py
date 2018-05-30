# links:https://leetcode.com/problems/sort-colors/description/
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color
# are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
# 题目大意：给定一个数组，只包含0,1,2三种元素，对该数组进行排

class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_pointer = -1
        two_pointer = len(nums)
        index = 0
        while index < two_pointer:
            if nums[index] == 1:
                index += 1
            elif nums[index] == 2:
                two_pointer -= 1
                nums[index], nums[two_pointer] = nums[two_pointer], nums[index]
            else:
                zero_pointer += 1
                nums[index], nums[zero_pointer] = nums[zero_pointer], nums[index]
                index += 1
        return nums


if __name__ == '__main__':
    s = Solution()
    r = s.sortColors([2, 0, 2, 1, 1, 0])
    print(r)
