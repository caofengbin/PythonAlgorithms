# links:https://leetcode.com/problems/reverse-integer/description/
# 给定一个32位的整数，将该整数进行翻转
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # step 1:判断相应的数值是否溢出
        if x > 2 ** 31 - 1:
            return 0

        if x == 0:
            return 0

        negate = 1 if x > 0 else -1
        n = abs(x)
        output = ''

        while n > 0:
            output += str(n % 10)
            n = n // 10
        output = int(output)
        if output > (2 ** 31 - 1):
            return 0
        return int(output) * negate


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(12345))
    print(s.reverse(-12345))
