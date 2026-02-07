# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

 

# 示例 1：

# 输入：root = [1,2,3,null,5,null,4]

# 输出：[1,3,4]



# 示例 2：

# 输入：root = [1,2,3,4,null,null,null,5]

# 输出：[1,3,4,5]



# 示例 3：

# 输入：root = [1,null,3]

# 输出：[1,3]

# 示例 4：

# 输入：root = []

# 输出：[]

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q =deque([root])
        res = []
        while q:
            size =len(q)
            for i in range(size):
                node =q.popleft()
                if i == (size-1):
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res 

# 记忆方法： 层序遍历维护队列，外循环得到子树长度，内循环遍历长度pop，如果是最后一个值就加到列表。

                
