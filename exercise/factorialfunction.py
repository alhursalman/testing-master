def factor(x):
    condition=True
    p=x
    i=1
    if x==0:
        print (x, " is a factorial number.")
    if x>=1:
        while condition==True:
            x = x/i
            if x==1:
                print (p, "is a factorial number. It is", i,"!.")
                condition==False
                break
            elif x<1:
                print (p, "is not a factorial number.")
                condition==False
                break
            else:
                i+=1
                
