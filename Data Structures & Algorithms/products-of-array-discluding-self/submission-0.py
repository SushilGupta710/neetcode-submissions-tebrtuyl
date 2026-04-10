class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #To get the product of array except itself then we need to dive the problem in left and right
        n=len(nums)
        left=[1]*n
        right=[1]*n
        result=[1]*n

        #First map the left side of array
        #why range is from 1 because we need to ignore 1st index value
        for i in range(1,n):
            left[i]=left[i-1]*nums[i-1]
        
        #Now map right side array
        #Range we are again skipping last element and getting second last and till -1 and then -1 is the step we need to take
        for i in range(n-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
        
        #Now get the product of left and right array and return the result
        for i in range(n):
            result[i]=left[i]*right[i]
        
        return result