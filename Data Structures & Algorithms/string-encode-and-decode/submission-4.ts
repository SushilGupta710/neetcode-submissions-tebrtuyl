class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs: string[]): string {
        var result=''
        for(var str of strs){
            result += str.length + "#" + str
        }
        return result;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str: string): string[] {
        var result=[]
        var i=0;
        while (i<str.length){
            var j = i
            while(str[j] !='#'){
                j++;
            }
            var length:number = Number(str.slice(i,j))
            var data = str.slice(j+1,j+1+length)
            result.push(data)
            i = j+1+length
        }
        return result
    }
}
