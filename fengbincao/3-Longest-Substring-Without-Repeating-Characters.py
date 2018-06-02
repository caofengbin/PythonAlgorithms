# links:https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Given a string, find the length of the longest substring without repeating characters.
# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# 寻找一个给定的字符串中，最长的无重复子串的长度

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left_window = 0
        right_window = -1
        result = -1
        statistics = [0] * 256
        cahr_list = list(s)

        while left_window < len(s):
            if right_window + 1 < len(s) and statistics[ord(cahr_list[right_window + 1])] == 0:
                right_window += 1
                index = ord(cahr_list[right_window])
                statistics[index] += 1
            else:
                index = ord(cahr_list[left_window])
                statistics[index] -= 1
                left_window += 1

            result = max(result, right_window - left_window + 1)

        if result == -1:
            return 0
        else:
            return result


if __name__ == '__main__':
    s = Solution()
    r1 = s.lengthOfLongestSubstring('pwwkew')
    print(r1)
    r2 = s.lengthOfLongestSubstring('bbbbb')
    print(r2)
    r3 = s.lengthOfLongestSubstring('abcabcbb')
    print(r3)