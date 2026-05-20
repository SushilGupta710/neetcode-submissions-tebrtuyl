public class Solution {
    public bool IsAnagram(string s, string t) {
        // define dictionary
        Dictionary <char,int> freq = new Dictionary<char,int>();

        // iterate through s element and increase the count
        foreach(var ch in s){
            freq[ch] = freq.GetValueOrDefault(ch) +1;
        }

        //iterate t element and reduce the count 
        foreach(var ch in t){
            if(!freq.ContainsKey(ch)){
                return false;
            }
            freq[ch] -=1;
        }

        //Now iterate through the dictionary and check the value
        foreach(var value in freq.Values){
            if(value != 0){
                return false;
            }
        }
        return true;
    }
}
