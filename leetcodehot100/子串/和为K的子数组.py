# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

# 子数组是数组中元素的连续非空序列。

 

# 示例 1：

# 输入：nums = [1,1,1], k = 2
# 输出：2
# 示例 2：

# 输入：nums = [1,2,3], k = 3
# 输出：2
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0]=1
        ans = 0
        pre = 0
        for x in nums:
            pre+=x 
            ans+=cnt[pre-k]
            cnt[pre]+=1
        return ans 

# 记忆方法： 和 二叉树部分路径总和III一起记，这题就是前缀和！ 初始 1 外加 标准3个+=！