class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        memory=[]
        for num in nums:
            if len(memory) >0 and num in memory:
                return True
            else:
                memory.append(num)
        return False
