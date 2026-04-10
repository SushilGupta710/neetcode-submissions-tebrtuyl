class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # defaultDists = defaultdict(list)
        # for num in nums:
        #     defaultDists[num].append(num)
        # sortedArray= sorted(defaultDists.items(),key=lambda item:len(item[1]),reverse=True)
        # result =[]
        # for s in range(k):
        #     result.append(sortedArray[s][0])

        # return result
        count = defaultdict(int)
        for n in nums:
            count[n]+=1
        #sorting the list
        sorted_item = sorted(count.items(),key= lambda x:x[1],reverse=True)
        print(sorted_item)

        #take top k element
        result = [item[0] for item in sorted_item[:k]]

        return result