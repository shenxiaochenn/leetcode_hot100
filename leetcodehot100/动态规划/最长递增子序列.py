# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

 
# 示例 1：

# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 示例 2：

# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 示例 3：

# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp =[1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
# 记忆方法： dp数组为以i结尾的序列，两循环一条件即完成！