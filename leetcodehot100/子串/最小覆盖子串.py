# 给定两个字符串 s 和 t，长度分别是 m 和 n，返回 s 中的 最短窗口 子串，使得该子串包含 t 中的每一个字符（包括重复字符）。如果没有这样的子串，返回空字符串 ""。

# 测试用例保证答案唯一。

 

# 示例 1：

# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
# 示例 2：

# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。
# 示例 3:

# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)> len(s):
            return ""
        cnt = Counter(t)
        missing = len(t)

        best_l =0
        best_lenth = float("inf")
        l =0

        for r,ch in enumerate(s):
            if cnt[ch]>0:
                missing-=1
            cnt[ch]-=1
            while missing==0:
                lenth = r-l+1
                if lenth< best_lenth:
                    best_lenth = lenth
                    best_l = l 
                out = s[l]
                if cnt[out] >=0:
                    missing+=1
                l+=1
                cnt[out]+=1
        return "" if best_lenth == float("inf") else s[best_l:best_l+best_lenth]
# 记忆方法： 右指针进：若 cnt[ch]>0 就 missing--，然后 cnt[ch]--；当 missing==0 就左指针缩：更新最优，再把 s[l] 还回去（cnt[out]++，若还回前 cnt[out]>=0 则 missing++），直到不满足。

# 和那个找到字符串中所有字母异味词一起看，一个思想。
