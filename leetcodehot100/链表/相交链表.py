# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

# 图示两个链表在节点 c1 开始相交：



# 题目数据 保证 整个链式结构中不存在环。

# 注意，函数返回结果后，链表必须 保持其原始结构 。


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a,b = headA,headB
        while a != b :
            a = a.next if a else headB
            b = b.next if b else headA
        return a 

# 记忆方法： 太简单了，不写了！