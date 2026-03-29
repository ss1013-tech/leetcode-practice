from typing import List
class Solution:
    def findAnagrams(self,s:str,p:str)->List[int]:
        if len(p)>len(s):
            return []
        
        res=[]
        need=[0]*26
        window=[0]*26

        #记录p中每个字符的频率
        for ch in p:
            need[ord(ch)-ord(a)]+=1

        left=0
        for right in range(len(s)):
            #记录s中每个字符的频率
            window[ord(s[right])-ord('a')]+=1
            #窗口长度>p, pop left
            if right-left+1>len(p):
                window[ord(s[left]) - ord('a')] -= 1
                left += 1
            if right - left + 1 == len(p) and window == need:
                res.append(left)
        return res

