# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

# 如果数组中不存在目标值 target，返回 [-1, -1]。

# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

 

# 示例 1：

# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 示例 2：

# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 示例 3：

# 输入：nums = [], target = 0
# 输出：[-1,-1]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def lower_bound(target):
            l=0
            r=len(nums)
            while l<r:
                middle = (l+r)//2
                if nums[middle]<target:
                    l =middle+1
                else:
                    r=middle
            return l
        return [lower_bound(target),lower_bound(target+1)-1] if target in nums else [-1,-1]

# 记忆方法： 找两个（target和target+1）下界！