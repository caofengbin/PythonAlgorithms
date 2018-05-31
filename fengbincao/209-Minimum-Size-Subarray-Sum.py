# links:https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # 初始化过程，[left_window, right_window]左闭右闭区间内，均属于滑动窗口的范围
        left_window = 0
        right_window = -1
        result = len(nums) + 1
        sum = 0

        while left_window < len(nums):
            if sum < s and right_window + 1 < len(nums):
                right_window += 1
                sum += nums[right_window]
            else:
                sum -= nums[left_window]
                left_window += 1
            if sum >= s:
                result = min(result, right_window - left_window + 1)

        if result == len(nums) + 1:
            return 0
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    print(r)
