# 给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

# 完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

 

# 示例 1：

# 输入：n = 12
# 输出：3 
# 解释：12 = 4 + 4 + 4
# 示例 2：

# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9

class Solution:
    def numSquares(self, n: int) -> int:
        nums = [i*i for i in range(1,101)]
        dp =  [float("inf")]*(n+1)
        dp[0] = 0
        dp[1] = 1
        for x in nums:
            for j in range(x,n+1):
                dp[j] = min (dp[j],dp[j-x]+1)
        return dp[n]

# 记忆方法： 这题是一个完全背包问题，因为求最小所以初始化正无穷，别习惯性0了！