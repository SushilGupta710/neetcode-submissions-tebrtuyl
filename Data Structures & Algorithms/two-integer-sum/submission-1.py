class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum=[]
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target and i!=j:
                    sum.append(i)
                    sum.append(j)
                    return sum
        return sum