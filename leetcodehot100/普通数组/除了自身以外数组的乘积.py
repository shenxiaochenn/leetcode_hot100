# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除了 nums[i] 之外其余各元素的乘积 。

# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

# 请 不要使用除法，且在 O(n) 时间复杂度内完成此题。

 

# 示例 1:

# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
# 示例 2:

# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre =  [1]
        post = [1]
        for x in nums:
            pre.append(x*pre[-1])
        for x in nums[::-1]:
            post.append(x*post[-1])
        pre = pre[:-1]
        post = post[:-1][::-1]
        return [x*y for x,y in zip(pre,post)]

# 记忆方法： 前缀积 * 后缀积 
