

def climbstairs(n):

    print(n)

    if n==1:
        print("hit1")
        return 1
    if n==2:

        print("hit2")

        return 2

    return climbstairs(n-1) + climbstairs(n-2)

print(climbstairs(5))

