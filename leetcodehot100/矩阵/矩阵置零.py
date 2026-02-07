# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

 

# 示例 1：


# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]
# 示例 2：


# 输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# 输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n =len(matrix[0])

        matrix_row_zero = any([ row[0]==0 for row in matrix])
        matrix_col_zero = any([ col==0 for col in matrix[0]])

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0 :
                    matrix[i][0] = 0
                    matrix[0][j] = 0  
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or  matrix[0][j] == 0:
                    matrix[i][j] = 0 
        if matrix_row_zero:
            for i in range(m):
                matrix[i][0] = 0
        if matrix_col_zero:
            for i  in range(n):
                matrix[0][i] = 0   

# 记忆方法： 这题和标准答案是不一样的。 先看第一行第一列有没有0，如果有标记一下！ 再看里面的，如果有0把第一行第一列对应的位置设置成0.
# 然后再把对应的行和列全设为0（这里range从1开始容易错）. 最后在处理第一行第一列。
