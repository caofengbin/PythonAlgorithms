# links:https://leetcode.com/problems/reverse-vowels-of-a-string/description/
# 将一个字符串中的元音字母(a,e,i,o,u)进行翻转

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        strList = list(s)
        beginPosition = 0
        endPosition = len(strList) - 1
        while beginPosition < endPosition:
            if self.isVowels(strList[beginPosition]) and self.isVowels(strList[endPosition]):
                strList[beginPosition], strList[endPosition] = strList[endPosition], strList[beginPosition]
                beginPosition += 1
                endPosition -= 1
            if not self.isVowels(strList[beginPosition]):
                beginPosition += 1
            if not self.isVowels(strList[endPosition]):
                endPosition -= 1
        return "".join(list(strList))

    def isVowels(self, targetChar):
        # python中是没有&&及||这两个运算符的，取而代之的是英文and和or
        return targetChar == 'A' or targetChar == 'a' or \
               targetChar == 'E' or targetChar == 'e' or \
               targetChar == 'I' or targetChar == 'i' or \
               targetChar == 'O' or targetChar == 'o' or \
               targetChar == 'U' or targetChar == 'u'


if __name__ == '__main__':
    s = Solution()
    r = s.reverseVowels("hello")
    print(r)
