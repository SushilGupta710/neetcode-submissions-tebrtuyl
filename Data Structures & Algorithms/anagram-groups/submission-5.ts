class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        var anagramDict = new Map<string,string[]>();

        for(const word of strs){
            var sortedWord = word.split('').sort().join('')
            if(anagramDict.has(sortedWord)){
                anagramDict.get(sortedWord).push(word)
            }else{
                anagramDict.set(sortedWord,[word])
            }
        }

        return Array.from(anagramDict.values())
    }
}
