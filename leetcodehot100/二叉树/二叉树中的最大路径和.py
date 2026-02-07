# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

# 路径和 是路径中各节点值的总和。

# 给你一个二叉树的根节点 root ，返回其 最大路径和 。

 

# 示例 1：


# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
# 示例 2：


# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")

        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)
            self.ans =  max(self.ans,node.val+left+right)
            return node.val + max(left,right)
        dfs(root)
        return self.ans 
 
#记忆方法：dfs 返回给父亲的是单边最大增益（node+max(left,right)），全局答案更新的是以当前点为拐点的三段和（left+node+right），负增益用 0 丢掉。