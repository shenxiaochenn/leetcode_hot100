# 给你一个链表数组，每个链表都已经按升序排列。

# 请你将所有链表合并到一个升序链表中，返回合并后的链表。

 

# 示例 1：

# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 示例 2：

# 输入：lists = []
# 输出：[]
# 示例 3：

# 输入：lists = [[]]
# 输出：[]

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(a,b):
            dummy = ListNode()
            cur=dummy
            while a and b:
                if a.val<=b.val:
                    cur.next =  ListNode(a.val)
                    a = a.next
                    cur =  cur.next
                else:
                    cur.next =  ListNode(b.val)
                    b = b.next
                    cur =  cur.next  
            cur.next = a if a else b 
            return dummy.next
        ans =None

        for ll in lists:
            ans = merge(ans,ll)
        return ans   

# 记忆方法： 正解用堆实现， 我这个虽然慢，但是好记！大佬可以用堆实现！
