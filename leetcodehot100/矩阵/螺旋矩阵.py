# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

 

# 示例 1：


# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：


# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res+=matrix.pop(0)
            matrix = [list(row) for row in zip(*matrix)]
            matrix = matrix[::-1]
        return res

#记忆方法： 这种解法不是正解但是代码量少便于理解， 主要就是矩阵用zip做转置然后整体倒置