# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
 

# 示例 1：

# 输入：s = "()"

# 输出：true

# 示例 2：

# 输入：s = "()[]{}"

# 输出：true

# 示例 3：

# 输入：s = "(]"

# 输出：false

# 示例 4：

# 输入：s = "([])"

# 输出：true

# 示例 5：

# 输入：s = "([)]"

# 输出：false

class Solution:
    def isValid(self, s: str) -> bool:
        c_dic ={"(":")","{":"}","[":"]"}

        l_ch = []

        for ch in s:
            if ch in c_dic:
                l_ch.append(c_dic[ch])
            else:
                if not l_ch:
                    return False
                r_ch = l_ch.pop()
                if r_ch != ch:
                    return False
        return l_ch==[]

#记忆方法：左括号：压入它对应的右括号；右括号：必须等于栈顶期望（两种情况哦！）。