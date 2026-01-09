## Two pointer problem : finding two integers in a sorted array thats adds up to a target value


a=[1,2,7,10]

target = 9


def sum_array(array_value,target_value):

    left=0
    right = len(array_value) -1


    while left < right:
        sum_val = array_value[left] + array_value[right]
     

        if sum_val==target:
            return  [left,right]
            
        elif sum_val < target:

            left=left+1
        else:

            right=right-1
    return []

print(sum_array(a,target))




