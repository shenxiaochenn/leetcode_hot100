# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



 

# 示例 1：

# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 示例 2：

# 输入：digits = "2"
# 输出：["a","b","c"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []
        path = []

        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def dfs(idx):
            if idx ==len(digits):
                res.append("".join(path[:]))
                return 
            for ch in phone[digits[idx]]:
                path.append(ch)
                dfs(idx+1)
                path.pop()
        dfs(0)

        return res 

# 记忆方法： 回溯，收集末尾叶子节点的答案！idx代表第几层啦！
