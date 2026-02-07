# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

 

# 示例 1：


# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
# 示例 2：



# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k<=1:
            return head
        node =head
        for _ in range(k):
            if not node:
                return head 
            node = node.next 
        pre  = None
        cur = head
        for _ in range(k):
            cur.next, pre, cur =  pre,cur,cur.next 
        head.next = self.reverseKGroup(cur,k)
        return pre 

# 记忆方法： 这题用递归解，代码量少！ 两个range k，然后翻转链表 （head是上一个链表的尾部，cur是下一个链表的头）