# 给你一个二叉树的根节点 root ， 检查它是否轴对称。

 

# 示例 1：


# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 示例 2：


# 输入：root = [1,2,2,null,3,null,3]
# 输出：false

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(left,right):
            if not left and not right:
                return True
            if not left or not right: 
                return False
            if left.val != right.val:
                return False
            return mirror(left.left,right.right) and mirror(left.right,right.left)

        return mirror(root.left,root.right)

# 记忆方法： 镜子函数，后序遍历！