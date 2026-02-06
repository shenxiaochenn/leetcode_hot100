# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

 

# 示例 1：

# 输入：nums = [1,1,1,2,2,3], k = 2

# 输出：[1,2]

# 示例 2：

# 输入：nums = [1], k = 1

# 输出：[1]

# 示例 3：

# 输入：nums = [1,2,1,2,1,2,3,1,3,2], k = 2

# 输出：[1,2]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [a for a,_ in Counter(nums).most_common(k)]
# 记忆要点： counter 配合 most_common 秒杀 