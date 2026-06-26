class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsFrequency = {}
        ans = []

        for n in nums:
            numsFrequency[n] = 1 + numsFrequency.get(n, 0)


        numsFrequencySorted = dict(sorted(numsFrequency.items(), key=lambda item: item[1], reverse=True))
        
        count = 1
        for n, frequency in numsFrequencySorted.items():
                ans.append(n)
                count += 1
                if count > k:
                    break
        
        return ans