# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

 

# 示例 1:

# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
# 示例 2:

# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:

# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        l = 0
        ans = 0
        for r,ch in enumerate(s):
            if ch in last and last[ch] >=l:
                l=last[ch]+1
            last[ch] =r
            ans = max(ans,r-l+1)
        return ans 

# 记忆方法：查重复 → 挪左端 → 记位置 → 更答案