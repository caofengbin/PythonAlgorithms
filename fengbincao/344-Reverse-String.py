# links:https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


if __name__ == '__main__':
    s = Solution()
    r = s.reverseString("12345aa")
    print(r)