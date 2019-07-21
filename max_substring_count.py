def lengthOfLongestSubstring(s: str) -> int:
    dic = {}
    max_sub_count = 0
    cur_count = 0
    prev_index = 0
    cur_index = 0


    while len(s) > cur_index:
        cur_char = s[cur_index]
        if cur_char not in dic:
            dic[cur_char] = None
            cur_index += 1

            cur_count += 1
            if cur_count > max_sub_count:
                max_sub_count = cur_count

        else:
            dic.clear()
            cur_count = 0
            prev_index = prev_index + 1
            cur_index = prev_index


    return max_sub_count

def lengthOfLongestSubstring(s):
        d,m,c,st={},0,0,0
        for i, e in enumerate(s):
            if e in d and d[e] >= st:
                m = max(m,c)
                c = i - d[e]
                st = d[e] + 1
            else:
                c += 1
            d[e] = i
        return max(m,c)



def max_substring_count(s):
    dict = {}
    max_val = 0
    prev_index = 0
    cur_count = 0

    for index, chr in enumerate(s):
        '''
        check if the current letter is an existing key in the dictionary and

        '''

        if chr in dict and dict[chr] >= cur_count:
            max_val = max(max_val, count)
            # print('max val => ', max_val)

            prev_index = index - dict[chr]
            # print('count => ', count)

            cur_count = dict[chr] + 1
            # print('current count => ', cur_count)
        else:
            prev_index += 1

        dict[chr] = index
        # print(max_val, count)
        # print(dict)



def main():
    text = "pwwkew"
    print(max_substring_count(text))
    # print(lengthOfLongestSubstring(text))



if __name__ == '__main__':
    main()
