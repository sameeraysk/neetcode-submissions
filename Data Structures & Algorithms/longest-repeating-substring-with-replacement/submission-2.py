class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        count={}
        max_freq=0
        max_len=0
        left=0
        for i in range(n):
            count[s[i]]=count.get(s[i],0)+1
            max_freq=max(max_freq,count[s[i]])
            if (i - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, i - left + 1)

                    
        return max_len


