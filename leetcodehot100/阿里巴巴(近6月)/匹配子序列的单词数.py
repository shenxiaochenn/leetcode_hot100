# 给定字符串 s 和字符串数组 words, 返回  words[i] 中是s的子序列的单词个数 。

# 字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。

# 例如， “ace” 是 “abcde” 的子序列。
 

# 示例 1:

# 输入: s = "abcde", words = ["a","bb","acd","ace"]
# 输出: 3
# 解释: 有三个是 s 的子序列的单词: "a", "acd", "ace"。
# Example 2:

# 输入: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# 输出: 2
from bisect import bisect_right
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pos = defaultdict(list) 
        for idx , ch in enumerate(s):
            pos[ch].append(idx) 
        def string_set(w):
            cur = -1 
            for ch in w:
                lst = pos.get(ch)
                if not lst:
                    return False 
                k = bisect_right(lst,cur) 
                if k ==len(lst):
                    return False 
                cur = lst[k] 
            return True 
        return sum(string_set(w) for w in words)

# 记忆方法： 把 s 里每个字符出现的位置都存起来。检查一个 word 时，用二分找“下一个位置”。cur 是“上一次用掉的位置”，每次用二分在该字符的位置表里找“第一个比 cur 大的位置”。