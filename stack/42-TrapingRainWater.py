# stack
#我们维护一个 从栈底到栈顶高度递减 的栈。
from typing import List
class Solution:
    def trap(self, height:List[int]) -> int:
        water=0
        stack=[]
        for i in range(len(height)):
            while stack and height[i]>height[stack[-1]]:
                bottom=stack.pop() #坑底元素idx
                # 如果弹出后栈空了，说明没有左边界，不能接水
                if not stack:
                    break
                #现在找左边界
                left=stack[-1]
                #盛水量=height*width
                #height=min(左边界，现在的高度)-坑底的高度; 因为水取决于较小的高度-坑底的高度
                h=min(height[left],height[i])-height[bottom]
                width=i-left-1 #两个边界之间“中间的格子数”
                water+=width * h
            stack.append(i)
        return water
            

