public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var lookupDict = new Dictionary<int,int>();
        for (int i =0;i<nums.Length;i++){
            int diff = target-nums[i];
            if(lookupDict.ContainsKey(diff)){
                return new int[] {lookupDict[diff],i};
            }
            lookupDict[nums[i]] = i;
        }
        return new int[] {};
    }
}
