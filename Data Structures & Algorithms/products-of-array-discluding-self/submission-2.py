class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #first we need length of nums
        length = len(nums)
        #define result with default value as 1
        result = [1] * length

        #First we will get all the left product and store it into result
        for i in range(1,length):
            result[i] = result[i-1] * nums[i-1]
        
        #Now here we need to get right product but while getting we will compute it with result
        #we need to get array element from right
        #defining right as 1
        right=1
        for i in range(length-1,-1,-1):
            result[i]*=right
            right*=nums[i]
        return result
