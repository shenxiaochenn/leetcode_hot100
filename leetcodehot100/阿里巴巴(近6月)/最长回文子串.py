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
        # n =len(s)
        # self.ans = ""

        # def expand(l,r):
        #     while l>=0 and r<n and s[l]==s[r]:
        #         if r-l+1 > len(self.ans):
        #             self.ans = s[l:r+1]
        #         l-=1
        #         r+=1
        # for c in range(n):
        #     expand(c, c)  
        #     expand(c, c+1)
        # return self.ans
        n =len(s)  
        dp = [[False]*n for _ in range(n)] 
        start = 0
        best_len = 1
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > best_len:
                        start = i 
                        best_len =j-i+1   
        return s[start:start+best_len]
