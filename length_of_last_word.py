class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        word = ''
        size = 0
        # A BOOLEAN THAT IS SET TO TRUE WHEN WE SEE THE FIRST LETTER
        isWord = False
        counter = 0
        if len(s) == 0 or s == ' ':
            return 0
        if len(s) == 1:
            return 1

        for i in range(len(s) - 1, -1, -1):
            chr = s[i]

            # CHECKING IF VALID LETTER AND WE HAVENT SEEN A LETTER YET
            # if chr.isalpha() == True and isWord == False:
            #     counter += 1
            # else:
            #     isWord = True

            if chr.isalpha() == False and isWord == False:
                continue

            elif chr.isalpha():
                isWord = True
                counter += 1

            else:
                return counter

        return counter
