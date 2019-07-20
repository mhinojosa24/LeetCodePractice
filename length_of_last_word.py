class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = ''
        size = 0

        if len(s) == 0 or s == ' ':
            return 0
        if len(s) == 1:
            return 1

        for i in range(len(s) - 1, -1, -1):
            chr = s[i]

            if chr.isspace() == True and s:
                continue
            elif chr.isalpha() == True:
                size += 1

            print(chr.isspace())
            print(chr.isalpha())
