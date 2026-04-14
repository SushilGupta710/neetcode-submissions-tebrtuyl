class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #solution 1 with O(n^2) because check with tow loop
        #step 1- Run the outer i loop till second last
        for i in range(len(nums)-1):
            #step 2- Run inner loop from 1 and till last
            for j in range(1,len(nums)):
                if(i!=j and nums[i]+nums[j]== target):
                    return [i,j]
        return []
