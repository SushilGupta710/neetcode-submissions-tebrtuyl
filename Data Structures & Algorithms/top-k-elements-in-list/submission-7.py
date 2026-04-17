class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groupDict={}

        for num in nums:
            groupDict[num]=groupDict.get(num,0)+1
        
        sortedData= sorted(groupDict.items(),key=lambda x:x[1],reverse=True)
        return [item[0] for item in sortedData[:k]]