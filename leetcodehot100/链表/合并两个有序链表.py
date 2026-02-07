# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

# 示例 1：


# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 示例 2：

# 输入：l1 = [], l2 = []
# 输出：[]
# 示例 3：

# 输入：l1 = [], l2 = [0]
# 输出：[0]

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy =ListNode()
        cur =dummy
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = ListNode(list1.val)
                list1,cur = list1.next,cur.next
            else:
                cur.next = ListNode(list2.val)
                list2,cur = list2.next,cur.next
        cur.next = list1 if list1 else list2

        return dummy.next

# 记忆方法： 标准代码，直接背诵，其他题也能用到