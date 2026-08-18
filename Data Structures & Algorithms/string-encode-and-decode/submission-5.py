class Solution:

    def encode(self, strs: List[str]) -> str:

        encode = ""
        for word in strs:
            encode += str(len(word)) + "#" + word
            
        return(encode)


    def decode(self, s: str) -> List[str]:
        
        decode = []
        i = 0
        j = 0

        while i  < len(s):
            if s[j] == "#":
                length = int(s[i:j])
                decode.append(s[j+1:j+length+1])
                j += (length + 1)
                i = j

            else:
                j += 1

        return(decode)



        

