class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #this way will have TC- 0(n log n)
        # because here we need to use sort and for loop
        #SC- 0(n) because we are storing the value in variable

        #first we need a dictionary which will hold the key and value and value are unique from array
        wordDict = {}

        #iterate the strs and sort the each word and add it into wordDict
        for word in strs:
            #to sort string we need to use join
            sortedWord = ''.join(sorted(word))
            #now add key as sortedWord and value as word
            #in normal list we need to assign a default valu so that it will not throw any error
            wordDict.setdefault(sortedWord,[]).append(word)
        
        #now we got all the groupanagram in my wordDictionary we need all the value
        return list(wordDict.values())