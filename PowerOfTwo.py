def powerOfTwo(n):    
    i=1
    while i<=n:
        if i==n:
            return True
        i=i*2
    return False

if (powerOfTwo(15)):
    print("True")
else:
    print("false")
