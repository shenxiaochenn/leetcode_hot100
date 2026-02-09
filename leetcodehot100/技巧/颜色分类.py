# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

# 必须在不使用库内置的 sort 函数的情况下解决这个问题。

 

# 示例 1：

# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
# 示例 2：

# 输入：nums = [2,0,1]
# 输出：[0,1,2]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,low,high=0,0,len(nums)-1
        while i<=high:
            if nums[i]==0:
                nums[i],nums[low]=nums[low],nums[i] 
                low+=1
                i+=1
            elif nums[i]==1:
                i+=1
            elif nums[i]==2:
                nums[i],nums[high]=nums[high],nums[i]
                high-=1

# 记忆方法： 零丢左，一跳过，二扔右；i 看货，low 收零，high 收二。