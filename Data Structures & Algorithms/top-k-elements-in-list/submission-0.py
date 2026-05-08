class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter= {}
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        
        sorted_items = sorted(counter.items(), key = lambda x:x[1], reverse = True)
        ans = []
        for key in range(k):
            ans.append(sorted_items[key][0])
        return ans