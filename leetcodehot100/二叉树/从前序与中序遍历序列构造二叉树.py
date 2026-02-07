# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。


# 示例 1:


# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
# 示例 2:

# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mid_idx =  {v:k for k,v in enumerate(inorder)}
        self.pre = 0
        def dfs(left,right):
            if left > right:
                return 
            root =  TreeNode(preorder[self.pre])
            root_idx =  mid_idx[preorder[self.pre]]
            self.pre +=1
            root.left = dfs(left,root_idx-1)
            root.right = dfs(root_idx+1,right)
            return root 
        return dfs(0,len(preorder)-1)

# 记忆方法：前序拿根，中序切左右；区间空就停，勿忘加一。

        