# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。


# 示例 1：

# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 示例 2：

# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
# 示例 3：

# 输入：nums = [1]
# 输出：[[1]]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n =len(nums)
        used = [False]*n

        def bt():
            if len(path)==n:
                res.append(path[:])
            for i in range(n):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                bt()
                used[i] = False
                path.pop()
        bt()
        return res 
# 记忆方法： 标准回溯代码！ 回溯的关键在于剪枝，每一个bt是深度，每一个for循环是宽度。


