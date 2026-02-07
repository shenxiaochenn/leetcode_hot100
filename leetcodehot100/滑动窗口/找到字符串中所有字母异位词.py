# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

# 示例 1:

# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#  示例 2:

# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt = Counter(p)
        lenth =  len(p)
        missing = len(p)
        l=0
        res = []
        for r,ch in enumerate(s):
            if cnt[ch] > 0:
                missing-=1
            cnt[ch]-=1
            if r-l+1>lenth:
                out = s[l]
                if cnt[out] >= 0:
                    missing+=1
                cnt[out]+=1
                l+=1        
            if r-l+1 == lenth and missing ==0:
                res.append(l)
        return res 

#记忆方法：右进：能补缺就 missing--，cnt--；超长（r-l+1）就左出：若出的是‘刚好需要的’就 missing++，cnt++；长度够且 missing==0 记录答案。

# 谈恋爱讲究恰到好处就像一个滑动窗口，你有一个理想型，符合就是missing--,超出就要看你心中的规则，若是你需要的就missing++