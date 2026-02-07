# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

 

# 示例 1：


# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 示例 2：

# 输入：head = []
# 输出：[]
# 示例 3：

# 输入：head = [1]
# 输出：[1]

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while prev.next and prev.next.next:
            a = prev.next
            b =prev.next.next
            a.next = b.next
            b.next = prev.next
            prev.next = b

            prev =a 
        return dummy.next

# 记忆方法： 三步交换，一步推进，注意条件！初始pre not cur！