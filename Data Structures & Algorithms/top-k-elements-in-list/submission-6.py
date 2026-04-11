class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(int)
        # here we store the unique value in hash dictionary
        for n in nums:
            result[n]+=1
        
        sortedData = sorted(result.items(),key=lambda x:x[1],reverse=True)
        return [item[0] for item in sortedData[:k]]
        


