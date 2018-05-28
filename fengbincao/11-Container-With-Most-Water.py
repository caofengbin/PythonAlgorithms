# https://leetcode.com/problems/container-with-most-water/description/
# 题目大意：
# 给定一个数组，数组元素的值表示竖线的高度，找两条竖线然后这两条线以及X轴构成的容器能容纳最多的水。

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # leftBar,riehtBar分别表示左边和右边最高的柱子，目标是寻找到leftBar左边没有比他高的柱子
        # riehtBar右边没有比他高的柱子
        leftBar = 0
        rightBar = len(height) - 1

        # 分别寻找的左边最高的柱子，以及右边最高的柱子
        leftMax = height[leftBar]
        rightMax = height[rightBar]

        result = -1
        maxArea = -1

        while leftBar < rightBar:
            if leftMax < rightMax:
                maxArea = (rightBar - leftBar) * leftMax
                leftBar += 1
                if leftMax < height[leftBar]:
                    leftMax = height[leftBar]
            else:
                maxArea = (rightBar - leftBar) * rightMax
                rightBar -= 1
                if rightMax < height[rightBar]:
                    rightMax = height[rightBar]

            if maxArea > result:
                result = maxArea

        return result


if __name__ == '__main__':
    s = Solution()
    r = s.maxArea([0, 1, 0, 3, 12])
    print(r)
