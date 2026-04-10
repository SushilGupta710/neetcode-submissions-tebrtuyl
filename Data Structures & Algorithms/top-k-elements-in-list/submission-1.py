class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        defaultDists = defaultdict(list)
        for num in nums:
            defaultDists[num].append(num)
        sortedArray= sorted(defaultDists.items(),key=lambda item:len(item[1]),reverse=True)
        result =[]
        for s in range(k):
            result.append(sortedArray[s][0])

        return result