from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #initial hashmap to store val index if haven't see that val
        hashmap={}
        #iterate through nums, check if remain has already exist
        #if exist, return; else put current number in hashmap
        for i, num in enumerate(nums):
            remain=target-num
            if remain not in hashmap:
                hashmap[num]=i
            else:
                return [i,hashmap[remain]]

sol = Solution()
nums = [2, 7, 11, 15]
target=9
res=sol.twoSum(nums,target)
print(res)
