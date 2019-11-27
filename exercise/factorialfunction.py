def factor(x):
    condition=True
    p=x
    i=1
    if x==0:
        return "True"
    if x>=1:
        while condition==True:
            x = x/i
            if x==1:
                return "True"
                condition==False
                break
            elif x<1:
                return "False"
                condition==False
                break
            else:
                i+=1
                
