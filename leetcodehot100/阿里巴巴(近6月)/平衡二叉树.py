# 给定一个二叉树，判断它是否是 平衡二叉树  

 

# 示例 1：


# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
# 示例 2：


# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
# 示例 3：

# 输入：root = []
# 输出：true


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            if not node:
                return 0
            left =  get_height(node.left)
            right =  get_height(node.right)
            if left==-1 or right==-1 or abs(left-right)>1:
                return -1
            return 1+ max(left,right)
        return get_height(root) != -1
