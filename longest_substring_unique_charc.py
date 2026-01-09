'''Question:** Find the length of the longest substring with all unique characters.

Input: s = "abcabcbb"
Output: 3
Explanation: "abc" is the longest (length 3)

Input: s = "bbbbb"
Output: 1
Explanation: "b" is the longest (length 1)

Input: s = "pwwkew"
Output: 3
Explanation: "wke" is the longest (length 3)

'''


def find_str(str_val):

    left=0
    right=0

    char_index={}

    max_sum =0


    for right, char in enumerate(str_val):


        if char in char_index and char_index[char] >=left:

            #if duplicate character is found and the character index is found further from the left

            left=char_index[char]+1  ##update left only when duplicate found from the duplicate index
            

        char_index[char] = right   ##move the char index further

        max_sum = max(max_sum,right-left+1)

        return max_sum

