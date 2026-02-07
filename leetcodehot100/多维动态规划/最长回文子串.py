# 给你一个字符串 s，找到 s 中最长的 回文 子串。

 

# 示例 1：

# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：

# 输入：s = "cbbd"
# 输出："bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        start_index = 0
        max_length = 1
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] ==s[j]:
                    if j-i <=2:
                        dp[i][j] = True
                    else:
                        dp[i][j] =  dp[i+1][j-1]
                if dp[i][j] and j-i+1 > max_length:
                    start_index = i 
                    max_length = j-i+1
        return s[start_index:start_index+max_length]

# 记忆方法： 双循环，首倒序，两条件判断。dp[i][j]：s[i..j] 是否回文！
# 
# 这题我这么写并不标准，但是可以AC,少了条件判断，例如dp[i][i] = True 因为隐进dp j了。