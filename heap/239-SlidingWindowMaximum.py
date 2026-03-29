#堆解法
import heapq
class Solution:
    def maxSlidingWindow(self,nums:[List],k:int) -> List[int]:
        heap=[]
        res=[]
        for i, num in enumerate(nums):
            heapq.heappush(heap,(-num,i))
            #形成窗口后开始记录答案
            if i>=k-1:
                #当heap[0][1]<=i-k,即栈顶的元素已经不属于窗口范围，弹出
                while heap[0][1]<=i-k:
                    heapq.heappop(heap)
                res.append(heap[0][0]*(-1))
        return res

#单调队列解法(最优解)

#队列里存的是 下标
#队头 q[0] 始终是当前窗口内最大的那个元素的下标
#如果队头下标已经不在窗口内，就把它弹出
#新元素进来前，把所有比它小的队尾元素都删掉，因为它们以后不可能成为窗口最大值
#这样队列从头到尾对应的值始终单调递减，所以队头就是当前窗口最大值

from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self,nums:[List],k:int) -> List[int]:
        q=deque()
        res=[]

        for i in range(len(nums)):
            #if front of q is out of window, pop
            if q and q[0]<=i-k:
                q.popleft()
            #if end of q less than nums[i], pop
            while q and nums[q[-1]]<nums[i]:
                q.pop() #这里是把队尾pop
            #append current nums
            q.append(nums[i])
            #if window form, record answer
            if i>=k-1:
                res.append(nums[q[0]])
        return res
