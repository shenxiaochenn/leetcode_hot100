# 给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。例如，字符串 "ababcc" 能够被分为 ["abab", "cc"]，但类似 ["aba", "bcc"] 或 ["ab", "ab", "cc"] 的划分是非法的。

# 注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。

# 返回一个表示每个字符串片段的长度的列表。

 

# 示例 1：
# 输入：s = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。 
# 示例 2：

# 输入：s = "eccbbbbdec"
# 输出：[10]

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        far = 0
        start = 0
        ch_far =  {ch:idx for idx,ch in enumerate(s)}
        res = []

        for idx,ch in enumerate(s):
            far = max(far,ch_far[ch])
            if idx == far:
                res.append(far-start+1)
                start =idx +1
        return res 


#记忆方法： 维护最远哈希表，达到最远的地方就添加进去，更新start

                

                