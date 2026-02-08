# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
 

# 示例 1：

# 输入：nums = [1,2,0]
# 输出：3
# 解释：范围 [1,2] 中的数字都在数组中。
# 示例 2：

# 输入：nums = [3,4,-1,1]
# 输出：2
# 解释：1 在数组中，但 2 没有。
# 示例 3：

# 输入：nums = [7,8,9,11,12]
# 输出：1
# 解释：最小的正数 1 没有出现。

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for idx in range(n):
            while 0< nums[idx] < n+1:
                correct_idx =  nums[idx] -1
                if  nums[idx] == nums[correct_idx]:
                    break
                else:
                    nums[idx],nums[correct_idx] =  nums[correct_idx],nums[idx] 
        for idx in range(n):
            if nums[idx] != (idx+1) :
                return idx+1
        return n+1 

# 记忆方法： 

# 把数组当成停车场：
# 数字 x 的车应该停在 x-1 号车位。
# 只要当前位置的车 x 合法（1..n），就把它交换到它该去的车位。
# 直到当前位置停的不是合法车，或者要去的车位已经停着同款车（重复）。
# 最后再扫一遍：第一个 nums[i] != i+1 的位置，说明 i+1 这辆车根本没来。

