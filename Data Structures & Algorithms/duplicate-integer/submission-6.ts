class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        let seenSet = new Set<number>()
        for(const x of nums){
            if(seenSet && seenSet.has(x)){
                return true
            }
            seenSet.add(x)
        }
        return false
    }
}
