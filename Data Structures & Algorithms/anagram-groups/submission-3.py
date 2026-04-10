class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for w in strs:
            sortedWord = ''.join(sorted(w))
            result[sortedWord].append(w)
        return list (result.values())