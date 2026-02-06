# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

# 请必须使用时间复杂度为 O(log n) 的算法。

 

# 示例 1:

# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
# 示例 2:

# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
# 示例 3:

# 输入: nums = [1,3,5,6], target = 7
# 输出: 4 

### 申小忱总结：  二分法！ 找边界，开区间（左闭右开）！ 找下标，闭区间（左闭右闭）！ 这题一看就是找边界！

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        while l<r:
            mid =(r+l)//2
            if nums[mid] <target:
                l = mid+1
            else:
                r = mid  
        return l  
    
# 记忆方法： 标准找下界的代码，开区间找下界



