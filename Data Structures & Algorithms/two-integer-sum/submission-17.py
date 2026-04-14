class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #here is TC-O(n) and SC-O(k)
        #creating the dictionary because we need to store the value and index
        indexDict = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in indexDict:
                return [indexDict[diff],i]
            indexDict[nums[i]]=i
        return []
