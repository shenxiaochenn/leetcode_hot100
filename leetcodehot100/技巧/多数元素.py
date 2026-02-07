# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

# 示例 1：

# 输入：nums = [3,2,3]
# 输出：3
# 示例 2：

# 输入：nums = [2,2,1,1,1,2,2]
# 输出：2

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate =None
        count =0
        for x in nums:
            if count ==0:
                candidate =x
                count =1
            elif x==candidate:
                count+=1
            else:
                count-=1
        return candidate

# 记忆方法： 同党加一、敌人减一；票数清零就换领袖。