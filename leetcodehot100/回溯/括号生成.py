# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

# 示例 1：

# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 示例 2：

# 输入：n = 1
# 输出：["()"]


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        res = []
        def bt(left,right):
            if len(path) == 2*n :
                res.append("".join(path[:]))  
            if left < n :
                path.append("(")
                bt(left+1,right)
                path.pop()
            if right < left: 
                path.append(")")
                bt(left,right+1)
                path.pop() 
        bt(0,0)
        return res   

# 记忆方法： 双分支回溯，放不放左括号（< n），放不放右括号(< right)。


# 因为这题的“选择空间”不是一个候选数组 candidates，而是每一步只有两种固定动作：放 "(" 或放 ")"。
# for 循环的本质是：在一堆候选里挑一个；但这里每层根本没有“一堆”，只有“能不能放左括号？”、“能不能放右括号？”这两个布尔分支。