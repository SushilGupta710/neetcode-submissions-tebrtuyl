class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenSet=set() #declare set becaue we need to store unique value
        for num in nums:
            #checking if number is there in set then return True directly
            if num in seenSet:
                return True
            #else we need to add it in set
            else:
                seenSet.add(num)
        return False