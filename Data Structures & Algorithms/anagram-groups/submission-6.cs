public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var anargamDict = new Dictionary<string,List<string>>();

        foreach(var word in strs){
            var sortedWord = new string(word.OrderBy(x=>x).ToArray());
            if(anargamDict.ContainsKey(sortedWord)){
                anargamDict[sortedWord].Add(word);
            }else{
               anargamDict[sortedWord] = new List<string>{word}; 
            }
        }

        var result = anargamDict.Values.ToList();
        return result;
    }
}
