# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

 

# 示例 1：


# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 示例 2：

# 输入：n = 1
# 输出：[["Q"]]

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [["."]*n for _ in range(n)]
        cols = [False]*n
        diag_1 = [False]*(2*n-1)
        diag_2 = [False]*(2*n-1)
        res = []
        def bt(r):
            if r==n:
                res.append(["".join(row) for row in grid])  
            for c in range(n):
                diag1 = r-c+n-1
                diag2 = r+c
                if cols[c] or diag_1[diag1] or diag_2[diag2]:
                    continue
                grid[r][c]="Q"
                cols[c] =True
                diag_1[diag1] = True
                diag_2[diag2] = True
                bt(r+1)
                cols[c] =False
                diag_1[diag1] = False
                diag_2[diag2] = False
                grid[r][c]="."
        bt(0)
        return res
# 记忆方法： 这题思想比较简单，如果当难题考简直血赚！  

