
num=15
def srt(x):


    left=1
    right=x
    while left<=right:

        mid = (left+right)//2


        sqr_val = mid*mid
    
        if sqr_val==x:
            return mid
    
        if x<sqr_val:
            right=mid-1
         
        else:
            left=mid+1
    return right

print(srt(num))