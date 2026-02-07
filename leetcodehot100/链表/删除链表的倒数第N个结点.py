# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

 

# 示例 1：


# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
# 示例 2：

# 输入：head = [1], n = 1
# 输出：[]
# 示例 3：

# 输入：head = [1,2], n = 1
# 输出：[1]

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy =ListNode()
        dummy.next =head 
        slow =fast =dummy
        for _ in range(n):
            fast =fast.next
        while fast.next:
            slow =slow.next
            fast =fast.next
        slow.next =slow.next.next
        return dummy.next 

# 记忆方法：快慢指针，快指针先走n步，然后一起走，快到None,慢就跳！
 