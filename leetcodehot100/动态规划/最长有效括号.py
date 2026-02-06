# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号 子串 的长度。

# 左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，比如 "(()())"。

 

# 示例 1：

# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
# 示例 2：

# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
# 示例 3：

# 输入：s = ""
# 输出：0

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack =[-1]
        ans =0
        for idx ,ch in enumerate(s):
            if ch =="(":
                stack.append(idx)
            else:
                stack.pop()
                if not stack:
                    stack.append(idx)
                else:
                    ans =max(ans,idx-stack[-1])
        return ans 

# 记忆方法： 这题用栈解，初始化-1栈，左括号压栈，右括号讨论！