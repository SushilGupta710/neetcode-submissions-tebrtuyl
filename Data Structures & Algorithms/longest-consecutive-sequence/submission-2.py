class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #to store the unique and sequence order value with O(n) TC
        numSet = set(nums)
        result=0

        for num in numSet:
            #First here we need to check if num-1 is not exists in set then we need to track the longest sequence
            #So basically we need to check the start value is not present then track the length
            if num-1 not in numSet:
                length=0
                while (num+length) in numSet:
                    length+=1
                result = max(result,length)
        return result

