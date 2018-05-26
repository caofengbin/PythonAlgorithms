# links:https://leetcode.com/problems/move-zeroes/description/

# Given an array nums, write a function to move all 0's
# to the end of it while maintaining the relative order
# of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after
# calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nonZeroPointer = 0
        for index in range(len(nums)):
            if (nums[index] != 0):
                nums[nonZeroPointer] = nums[index]
                nonZeroPointer += 1
        for index2 in range(nonZeroPointer, len(nums)):
            nums[index2] = 0

        return  nums


if __name__ == '__main__':
    s = Solution()
    r = s.moveZeroes([0, 1, 0, 3, 12])
    print(r)
