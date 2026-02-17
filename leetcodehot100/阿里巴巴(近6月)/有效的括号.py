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
        cnt =  {"(":")","[":"]","{":"}"}
        stack =[]
        for ch in s :
            if  ch in cnt:
                stack.append(cnt[ch])
            else:
                if stack == []:
                    return False
                aa = stack.pop()
                if aa != ch :
                    return False
        return True if stack == [] else False
