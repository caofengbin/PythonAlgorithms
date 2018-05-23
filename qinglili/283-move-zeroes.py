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
class Solution:
    def movezeroes(self, nums: list):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) - 1 and nums[i] == 0:
                continue
            elif nums[i] == 0:
                tmp = nums[i]
                nums.pop(i)
                nums.append(tmp)

        return nums

if __name__ == '__main__':
    s = Solution()
    r = s.movezeroes([0, 0, 3, 8, 0, 12])
    print(r)
