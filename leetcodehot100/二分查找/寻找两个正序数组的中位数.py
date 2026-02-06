# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

# 算法的时间复杂度应该为 O(log (m+n)) 。

 

# 示例 1：

# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
# 示例 2：

# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        m,n = len(A),len(B)
        if  m>n:
            A,B,m,n = B,A,n,m
        left_count = (m+n+1)//2
        l =0
        r =m
        while l<=r:
            i = (l+r)//2
            j =  left_count - i
            A_left  = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i]     if i < m else float("inf")
            B_left  = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j]     if j < n else float("inf")

            if A_left<=B_right and B_left <= A_right:
                if (m+n)%2 ==1:
                    return max(A_left,B_left)
                else:
                    return (max(A_left,B_left) + min(A_right,B_right))/2
            elif A_right < B_left:
                l=i+1
            else:
                r=i-1
# 记忆方法：i 是 A 左半取的个数，范围 [0..m]。短数组上二分一个切口 i；j 由 left_count-i 得；看四个边界值，满足交叉有序就出答案，不满足就按 A_left 和 B_right 决定切口左右移动。