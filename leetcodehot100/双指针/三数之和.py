# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

# 示例 1：

# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
# 示例 2：

# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
# 示例 3：

# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n =len(nums)
        res = []
        for i in range(n-2):
            if nums[i]>0:
                break
            num_1 = nums[i]
            if i>0 and nums[i]==nums[i-1]:
                continue 
            l = i+1
            r = n-1
            while l<r:
                s = num_1 + nums[l] +nums[r]
                if s<0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    res.append([num_1,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] ==nums[l-1]:
                        l+=1
                    while l<r and nums[r] ==nums[r+1]:
                        r-=1
        return res 

# 记忆方法：排序 + 固定 i（跳过重复且 i>0 早停）+ 双指针找两数和 = -nums[i]，命中后 l/r 各自跳过重复