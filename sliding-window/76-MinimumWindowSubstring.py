from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t:str) -> str:
        #符合窗口的条件： t的所有字符类别都包括，并且c在S的频率>=freqT[c]
        #edge case: t 包含多于 s的字符
        if len(t)>len(s):
            return ""
        #需要的字符类别和数量
        freqT=Counter(t)
        need=len(freqT)
        formed=0

        left=0
        freqS=defaultdict(int)
        minLength=float('inf')
        minStr=""
        for i, c in enumerate(s):
            freqS[c]+=1
            #当s中的字符频率和t中的字符频率相等时，说明形成一个类别的字符
            if c in freqT and freqS[c]==freqT[c]:
                formed+=1
            while formed == need:
                #记录minwindow
                if (i-left+1)<minLength:
                    minLength=i-left+1
                    minStr=s[left:i+1]
                
                leftChar=s[left]
                freqS[leftChar]-=1
                if leftChar in freqT and freqS[leftChar]<freqT[leftChar]:
                    formed-=1
                if freqS[leftChar]==0:
                    del freqS[leftChar]
                left+=1
        return minStr
              

        
