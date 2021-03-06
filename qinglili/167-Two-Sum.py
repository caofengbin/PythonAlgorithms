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
        :param numbers: list[int]
        :param trget: int
        :return: list[int]
        """
        tmpDict = {}
        for i in range(len(numbers)):
            item = numbers[i]
            if (target - item) in tmpDict:
                return (tmpDict[target-item] + 1, i + 1)
            tmpDict[item] = i

    def twoSum1(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while i < j:
            tmp = numbers[i] + numbers[j]
            if tmp == target:
                return [i + 1, j + 1]
            elif tmp > target:
                j -= 1
            elif tmp < target:
                i += 1

if __name__ == '__main__':
    s = Solution()
    l = s.twoSum1([2, 7, 11, 15],9)
    print(l)