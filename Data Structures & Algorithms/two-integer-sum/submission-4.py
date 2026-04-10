class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenSet={}
        for i,num in enumerate(nums):
            needed = target - num
            if needed in seenSet:
                return [seenSet[needed],i]
            else:
                seenSet[num]=i
        