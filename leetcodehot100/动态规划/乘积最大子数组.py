# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

# 测试用例的答案是一个 32-位 整数。

# 请注意，一个只包含一个元素的数组的乘积是这个元素的值。

 

# 示例 1:

# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:

# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = ans = nums[0]
        for x in nums[1:]:
            a = cur_max*x
            b = cur_min*x
            cur_max = max(a,b,x)
            cur_min = min(a,b,x) 
            ans = max(ans,cur_max)
        return ans 

# 记忆方法： 初始化3个值，一个循环结束！（dp数组比较麻烦）