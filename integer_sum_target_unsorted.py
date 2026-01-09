## finding integers that adds up to target value in an unsorted array

a=[1,9,2,4,6]

target = 13

def unsort_target(array_val,target):

    seen={}

    for i,num in enumerate(array_val):

        complement = target-num

        print(num,complement,seen)

        if complement in seen:
            return [complement,num]

        seen[num]=i

print(unsort_target(a,target))

    