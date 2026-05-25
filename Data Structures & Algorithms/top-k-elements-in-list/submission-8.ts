class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {

        //First define dictionary
        var eleDict = new Map<number,number>()

        //First we store or seggrigated the count and number into dictionary
        for(let num of nums){
            if(eleDict.has(num)){
                eleDict.set(num,eleDict.get(num)!+1)
            }else{
                eleDict.set(num,1)
            }
        }

        //Now we will again sort this dictionary
        const sortedDict = [...eleDict.entries()].sort((a,b)=>b[1]-a[1])

        //Now we need to get the k elemet from this sorted dictionary
        return sortedDict.slice(0,k).map((x)=>x[0])

    }
}
