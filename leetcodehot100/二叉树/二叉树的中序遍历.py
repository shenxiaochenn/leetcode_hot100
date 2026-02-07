# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。

 

# 示例 1：


# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
# 示例 2：

# 输入：root = []
# 输出：[]
# 示例 3：

# 输入：root = [1]
# 输出：[1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res= []
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res 
#记忆法： 前序 中左右 中序 左中右 后序 左右中