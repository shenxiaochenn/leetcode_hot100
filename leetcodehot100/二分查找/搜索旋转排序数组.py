# 整数数组 nums 按升序排列，数组中的值 互不相同 。

# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 向左旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 下标 3 上向左旋转后可能变为 [4,5,6,7,0,1,2] 。

# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

 

# 示例 1：

# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
# 示例 2：

# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
# 示例 3：

# 输入：nums = [1], target = 0
# 输出：-1

### 申小忱总结：  二分法！ 找边界，开区间（左闭右开）！ 找下标，闭区间（左闭右闭）！ 这题一看就是找下标！
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        while l<=r:
            middle = (l+r)//2
            if nums[middle] ==target:
                return middle
            left_sort = nums[l] <= nums[middle]
            if left_sort:
                in_left =  nums[l] <= target <nums[middle]

                if in_left:
                    r =middle-1
                else:
                    l = middle+1
            else:
                in_right =  nums[middle] < target <= nums[r]

                if in_right:
                    l =middle+1
                else:
                    r =  middle-1
        return -1
# 记忆方法： 先判断哪边有序（left_sort = nums[l] <= nums[middle]）再判断在哪边（in_left =  nums[l] <= target <nums[middle]），两步走战略！