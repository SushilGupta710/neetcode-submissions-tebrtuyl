public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        var eleDict = new Dictionary<int,int>();

        foreach (int num in nums){
            if(eleDict.ContainsKey(num)){
                eleDict[num]+=1;
            }else{
                eleDict[num]=1;
            }
        }

        //Sort the dict and convert into array
        List<KeyValuePair<int,int>> sortedList = eleDict.OrderByDescending(x=>x.Value).ToList();

        //Now get top element from this List
        return sortedList.Take(k).Select(x=>x.Key).ToArray();
        
    }
}
