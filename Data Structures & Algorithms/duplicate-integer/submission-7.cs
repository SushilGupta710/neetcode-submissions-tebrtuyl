public class Solution {
    public bool hasDuplicate(int[] nums) {
        // define empty hashSet
        var seenSet = new HashSet<int>();
        for (int i=0;i<nums.Length;i++){
            if(seenSet.Contains(nums[i])){
                return true;
            }
            seenSet.Add(nums[i]);
        }
        return false;
    }
}