class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {

        let lookUpDict = new Map<number,number>();

        for (let i =0;i<nums.length;i++){
            let diff= target-nums[i];
            if(lookUpDict.has(diff)){
                return [lookUpDict.get(diff),i]
            }
            lookUpDict.set(nums[i],i)
        }

    }
}
