#Two pointers
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        leftMax,rightMax=0,0
        water=0
        while left<right: #当 left == right 时，只剩一个位置，它没有左右两侧的边界，因此无法形成有效的容器来接水。
            #每个位置能接的水量取决于它左边最高和右边最高柱子的较小值。
            if height[left]<height[right]:
                leftMax=max(leftMax,height[left])
                water+=leftMax-height[left]
                left+=1
            else:
                rightMax=max(rightMax,height[right])
                water+=rightMax-height[right]
                right-=1
        return water

sol=Solution()
height=[4,2,0,3,2,5]
print(sol.trap(height))



