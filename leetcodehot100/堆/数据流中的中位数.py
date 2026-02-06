# 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

# 例如 arr = [2,3,4] 的中位数是 3 。
# 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
# 实现 MedianFinder 类:

# MedianFinder() 初始化 MedianFinder 对象。

# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。

# double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。

# 示例 1：

# 输入
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# 输出
# [null, null, null, 1.5, null, 2.0]

# 解释
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0



class MedianFinder:

    def __init__(self):
        self.low = []
        self.high = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low,-num)
        heapq.heappush(self.high,-heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low,-heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] +self.high[0])/2
        
# 记忆方法： 
# 加数三步：low<-x；low顶->high；high多了->low
# 取中位：low多：-low顶；一样多：(-low顶+high顶)/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()