class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        // create dictionary
        var freq:{[key:string]:number}={}

        // Now count the word from string s
        for (const ch of s){
            freq[ch] = (freq[ch] || 0) + 1 //assign default value
        }

        //Now here decrease the count from string t
        for (const ch of t){
            if(!freq[ch]){
                return false
            }
            freq[ch]-=1
        }

        //Now check all the count are zero or not
        for (const c in freq){
            if(freq[c] !== 0){
                return false
            }
        }
        return true
    }
}
