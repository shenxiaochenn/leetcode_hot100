# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

# 示例 1：

# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。

# 示例 2：

# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) %2 ==1:
            return False
        target = sum(nums)//2

        dp = [0]*(target+1)

        for i in nums:
            for j in range(target,i-1,-1):
                dp[j] = max(dp[j],dp[j-i]+i)
        return dp[target] == target

# 记忆方法： 这是一个01背包的问题，所以物品正序背包倒序，dp数组表示装这些货物最多的价值，此题价值等于货物重量！