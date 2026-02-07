# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

# 你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

 

# 示例 1 ：

# 输入：nums = [2,2,1]

# 输出：1

# 示例 2 ：

# 输入：nums = [4,1,2,1,2]

# 输出：4

# 示例 3 ：

# 输入：nums = [1]

# 输出：1

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # ll = Counter(nums)
        # for k,v in ll.items():
        #     if v ==1:
        #         return k
        ans = 0
        for x in nums:
            ans^=x 
        return ans

# 记忆方法： 我最开始想的是哈希表，结果正解是异或法！
# a ^ a = 0（自己和自己异或，归零）
# a ^ 0 = a（和 0 异或，不变）
# 异或满足交换律/结合律：顺序随便换
# 所以把所有数都 ^ 一遍，成对的就变成 0 被消掉，只剩单身狗。