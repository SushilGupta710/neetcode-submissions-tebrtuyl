class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode the string and put it into result
        result=""
        #for encode we use (length(s) + # + string) for better decoding and data redundent
        for s in strs:
            result+=str(len(s)) + '#' + s
        return result

    def decode(self, s: str) -> List[str]:
        i,result=0,[] # define result and i 
        while i < len(s):
        #now here we need to decode the string first we need to get the delemetor(#)
            j=i
            while s[j] !='#':
                j+=1#here we will get position of # value
            
            #now we need to get the length which we use to encode we know 
            #it it at first position of string
            length = int(s[i:j]) #type cast because it is number
            #now we know the length of string so throug this we can get the actual word from string
            #j+1 because j is pointing to # we need next value which is 1st letter of our string
            #j+1+length because we know our string start with j+1 but it's length is the length we get it previously
            word = s[j+1:j+1+length]

            #now we will append this word into the result
            result.append(word)

            #increase or point the i to the next string and again same step will repeat
            i=j+1+length
        return result

