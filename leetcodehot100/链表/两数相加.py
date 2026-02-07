# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

# 请你将两个数相加，并以相同形式返回一个表示和的链表。

# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 示例 1：


# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
# 示例 2：

# 输入：l1 = [0], l2 = [0]
# 输出：[0]
# 示例 3：

# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2:
            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0
            s = val_l1 +val_l2 + carry
            if s>= 10:
                s-=10
                carry =1
            else:
                carry=0
            cur.next =  ListNode(s)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur =cur.next
        if carry:
            cur.next = ListNode(carry)
        return dummy.next
# 记忆方法： 与合并列表区分，这个是or那个是and。这题多一个carry来传递数，注意把最后的数传下去，并且记得3个next！！！！
 