# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。


# 示例 1：

# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]

# 示例 2：

# 输入：root = [2,1,3]
# 输出：[2,3,1]

# 示例 3：

# 输入：root = []
# 输出：[]

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root 

# 记忆方法： 前序遍历，左右翻转。