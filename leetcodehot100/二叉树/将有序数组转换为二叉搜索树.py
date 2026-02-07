# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。

 

# 示例 1：


# 输入：nums = [-10,-3,0,5,9]
# 输出：[0,-3,9,-10,null,5]
# 解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

# 示例 2：


# 输入：nums = [1,3]
# 输出：[3,1]
# 解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree(left,right):
            if left > right:
                return
            middle = (left+right)//2
            root =  TreeNode(nums[middle])
            root.left = build_tree(left,middle-1)
            root.right = build_tree(middle+1,right)
            return root 
        return build_tree(0,len(nums)-1)

# 记忆方法： 二分法，前序遍历，这种想到中点的一般都是这样玩的。
