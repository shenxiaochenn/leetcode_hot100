# 给你一个满足下述两条属性的 m x n 整数矩阵：

# 每行中的整数从左到右按非严格递增顺序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。


# 示例 1：

# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true

# 示例 2：

# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false

### 申小忱总结：  二分法！ 找边界，开区间（左闭右开）！ 找下标，闭区间（左闭右闭）！ 这题一看就是找下标！

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0 
        r = m*n-1

        while l<=r:
            middle = (l+r)//2
            aa = matrix[middle//n][middle%n]

            if aa == target:
                return True 
            elif aa < target:
                l = middle+1
            else:
                r = middle-1
        return False 

# 记忆方法： 找下标闭区间，将矩阵转数组，找到mid值很关键！