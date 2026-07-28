class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for num in nums:
            if num in m:
                m[num]+=1
            else:
                m[num]=1
        sorted_items = sorted(m.items(), key = lambda x: x[1],reverse=True)
        l =[]
        for i in range(k):
            l.append(sorted_items[i][0])
        return l