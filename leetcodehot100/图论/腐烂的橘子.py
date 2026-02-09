# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

# 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

 

# 示例 1：



# 输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
# 示例 2：

# 输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个方向上。
# 示例 3：

# 输入：grid = [[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j)) 
        if fresh==0:
            return 0
        minunutes =0
        dir_ = [(0,1),(0,-1),(1,0),(-1,0)]
        while q and fresh>0:
            size = len(q)
            for _ in range(size):
                r,c =q.popleft()
                for dr,dc in dir_:
                    dir_r,dir_c=r+dr,c+dc
                    if  0<=dir_r<m and 0<=dir_c<n and grid[dir_r][dir_c]==1:
                        fresh-=1
                        q.append((dir_r,dir_c))
                        grid[dir_r][dir_c]=2
            minunutes+=1
        return minunutes if fresh==0 else -1

# 记忆方法：这题条件种类非常多，4个初始化可以和dir_的初始联系在一起记忆！ while -> size -> for -> r,c -> for ->  33(3条件和3操作)


