# 给定一个字符串 s ，请计算这个字符串中有多少个回文子字符串。

# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

 

# 示例 1：

# 输入：s = "abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
# 示例 2：

# 输入：s = "aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"


class Solution:
    def countSubstrings(self, s: str) -> int:
        # n = len(s) 
        # dp  = [[False]*n for _ in range(n)] 
        # ans = 0
        # for i in range(n-1,-1,-1):
        #     for j in range(i,n):
        #         if s[i]==s[j] and (j-i<3 or dp[i+1][j-1]):
        #             dp[i][j] = True
        #             ans+=1
        # return ans  
        n=len(s)
        self.ans = 0
        def expand(l,r):
            while l>=0 and r<n and s[l]==s[r]:
                self.ans+=1
                l-=1
                r+=1
        for i in range(n):
            expand(i, i) 
            expand(i, i+1)
        return self.ans
