# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（k 从 1 开始计数）。

# 示例 1：


# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
# 示例 2：


# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ans =None
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.k -=1
            if self.k == 0:
                self.ans = node.val
                return
            dfs(node.right)
        dfs(root)
        return self.ans 

