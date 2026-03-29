from collections import defaultdict
class Solution:
    def characterReplacement(self, s:str, k:str) -> int:
        longestLength=0
        freq=defaultdict(int)
        left=0
        maxfreq=0

        for i, c in enumerate(s):
            freq[c]+=1
            #最优解，提前记录maxfreq
            maxfreq=max(maxfreq,freq[c])
            #当窗口长度-max(freq.values())-> 剩余的需要替换的char > k, 需要弹出窗口
            while (i-left+1)-maxfreq>k:
                leftChar=s[left]
                freq[leftChar]-=1
                if freq[leftChar]==0:
                    del freq[leftChar]
                left+=1
            longestLength=max(longestLength,i-left+1)
        
        return longestLength