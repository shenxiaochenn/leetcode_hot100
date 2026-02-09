# 给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

 

# 示例 1：

# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
# 示例 2：

# 输入：s = "a"
# 输出：[["a"]]


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        res = []
        def bt(s):
            if not s:
                res.append(path[:])
            for i in range(len(s)):
                s1 = s[:i+1]
                if s1 != s1[::-1]:
                    continue
                path.append(s1)
                bt(s[i+1:])
                path.pop()
        bt(s)
        return res 

# 记忆方法 ： 从头切一段，回文才入栈；递归切剩下，空串就收案。