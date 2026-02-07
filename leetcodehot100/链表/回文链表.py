# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

 

# 示例 1：


# 输入：head = [1,2,2,1]
# 输出：true
# 示例 2：


# 输入：head = [1,2]
# 输出：false


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        ch_l = []
        while cur:
            ch_l.append(cur.val)
            cur = cur.next
        return ch_l==ch_l[::-1]
