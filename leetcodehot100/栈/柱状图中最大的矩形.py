# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

# 求在该柱状图中，能够勾勒出来的矩形的最大面积。


# 示例 1:

# 输入：heights = [2,1,5,6,2,3]
# 输出：10
# 解释：最大的矩形为图中红色区域，面积为 10
# 示例 2：

# 输入： heights = [2,4]
# 输出： 4

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] +heights +[0]
        st = [0]
        ans = 0

        for i in range(1,len(heights)):
            while heights[i] < heights[st[-1]]:
                mid =  st.pop()
                h = heights[mid]
                left = st[-1]
                w =  i-left-1
                ans = max(ans,w*h)
            st.append(i)
        return ans 
# 记忆方法： 单调递增栈，巧妙初始化，height+2,stack+1 !  高为mid,宽为i-left-1