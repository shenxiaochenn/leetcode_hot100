# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

# 示例 1：


# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
# 示例 2：

# 输入：root = [1]
# 输出：[[1]]
# 示例 3：

# 输入：root = []
# 输出：[]

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def bfs(node,depth):
            if not node:
                return
            if depth == len(res):
                res.append([])
            res[depth].append(node.val)
            bfs(node.left,depth+1)
            bfs(node.right,depth+1)
        bfs(root,0)
        return res 
# 记忆方法： 前序遍历，其实这里有一个回溯的过程，但是我写进函数里面了。这样好记一点儿！等于深度的时候加个列表，然后往里面装东西就可以了!