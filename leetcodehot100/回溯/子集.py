# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

# 示例 1：

# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 示例 2：

# 输入：nums = [0]
# 输出：[[],[0]]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        def bt(start_index):
            res.append(path[:])
            for i in range(start_index,len(nums)):
                path.append(nums[i])
                bt(i+1)
                path.pop()
        bt(0)
        return res 

# 记忆方法： 这题太简单了，我觉得这个start——index是关键，同时这个题的思想是每个叶子上的东西都要，不是只要末尾节点！