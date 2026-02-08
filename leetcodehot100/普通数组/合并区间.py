# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

# 示例 1：

# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2：

# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 示例 3：

# 输入：intervals = [[4,7],[1,4]]
# 输出：[[1,7]]
# 解释：区间 [1,4] 和 [4,7] 可被视为重叠区间。

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        start = intervals[0][0]
        end =  intervals[0][1]
        n = len(intervals)

        res = []

        for i in range(1,n):
            left = intervals[i][0]
            right = intervals[i][1]
            if left <= end:
                end =  max(end,right) 
            else:
                res.append([start,end])
                start = left 
                end = right  
        res.append([start,end])
        return res 
# 记忆方法： 想象你在射气球! 重叠的气球顺爆！  不要忘记收尾（最后append一下）！