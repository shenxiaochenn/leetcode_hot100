# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。


# 示例 1:

# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# 示例 2:

# 输入: numRows = 1
# 输出: [[1]]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp =  [[1]*i for i in range(1,numRows+1)]
        for i in range(2,numRows):
            for j in range(1,i):
                dp[i][j] = dp[i-1][j] +dp[i-1][j-1]
        return dp 
    
# 记忆方法： 这题我觉得做的时候，边界数值要想清楚，其实可以扩展成滚动数组（那时候你要倒序遍历j），如何他让你求某一行！


 