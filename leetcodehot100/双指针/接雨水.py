# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

# 示例 1：



# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
# 示例 2：

# 输入：height = [4,2,0,3,2,5]
# 输出：9

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        l = 0 
        r = len(height)-1
        max_left = height[0]
        max_right = height[-1]
        while l<r:
            if max_left <= max_right:
                ans += (max_left-height[l])
                l+=1
                max_left = max(max_left,height[l]) 
            else:
                ans += (max_right-height[r])
                r-=1
                max_right = max(max_right,height[r])
        return ans                  
# 记忆法：双指针  谁的最大边界更低就处理谁：更新该侧 max，再加 max - height，指针向内走