# links:https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target,
# where index1 must be less than index2.
#
# Note:
# 1.Your returned answers (both index1 and index2) are not zero-based.
# 2.You may assume that each input would have exactly one solution and you may not use the same element twice.


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        beginPosition = 0
        endPosition = len(numbers) - 1
        while beginPosition < endPosition:
            tmp = numbers[beginPosition] + numbers[endPosition]
            if tmp == target:
                return [beginPosition + 1, endPosition + 1]
            elif tmp > target:
                endPosition -= 1
            elif tmp < target:
                beginPosition += 1


if __name__ == '__main__':
    s = Solution()
    r = s.twoSum([0, 1, 0, 3, 12], 4)
    print(r)
