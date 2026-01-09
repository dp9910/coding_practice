arr = [2, 1, 5, 1, 3, 2]

k = 3


def slide_window(arr_val,k):

    window_sum = sum(arr[:k])  ##find the initial sum of the window

    max_sum = window_sum ##assign initial max sum


    ##since sum until 3rd index is already calculated, we start from there. eliminate first and add fourth index


    for i in range(k,len(arr_val)):
        
        ###sum of values of the window - the first index of thw windoew + new index on the right

        window_sum = window_sum - arr[i-k] +  arr[i]


        max_sum = max(max_sum,window_sum)

    return max_sum


print(slide_window(arr,k))