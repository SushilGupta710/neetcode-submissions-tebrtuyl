public class Solution {

    public string Encode(IList<string> strs) {
        string result = "";

        foreach(var str in strs){
            result+= str.Length + "#" + str;
        }
        return result;
    }

    public List<string> Decode(string s) {
        List<string> result = new List<string>();
        int i =0;
        while (i<s.Length){
            int j = i;

            while (s[j] != '#'){
                j++;
            }
            int lengthOfData = int.Parse(s.Substring(i,j-i));
            string data = s.Substring(j+1,lengthOfData);
            result.Add(data);
            i = j+1+lengthOfData;
        }
        return result;
   }
}
