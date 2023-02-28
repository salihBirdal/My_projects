x=2
if x==1 or x<=0:
    print("Not prime number")
else:
    for i in range(1,x):
        if i%x==0:
            print("Not Prime Number")
            break
    else:
        print("Prime Number")