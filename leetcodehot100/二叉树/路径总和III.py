# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

 

# 示例 1：



# 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# 输出：3
# 解释：和等于 8 的路径有 3 条，如图所示。
# 示例 2：

# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cum = defaultdict(int)
        cum[0] = 1                 # 关键：空前缀和出现一次
        self.ans =0 
        def dfs(node,sum_now):
            if not node:
                return 0
            sum_now+=node.val
            self.ans+=cum[sum_now-targetSum]
            cum[sum_now]+=1
            dfs(node.left,sum_now)
            dfs(node.right,sum_now)
            cum[sum_now]-=1
        dfs(root,0)
        return self.ans

# 记忆方法： 33法 ！ 方法三（哈希表，前缀和，回溯！） 三加和（sum_now,self.ans,cum[sum_now]）
