##find if a word is palindrome or not

str_test="A man, a plan, a canal: Panamas"


def palind_word(str_val):

    seen={}

    left = 0
    right = len(str_test)-1

    while left < right and not str_test[left].isalpha():

        left=left+1

    while left < right and not str_test[right].isalpha():

        right=right-1
    

    if str_test[left].lower()!=str_test[right].lower():

        return False

    left=left+1
    right=right-1

    return True

print(palind_word(str_test))