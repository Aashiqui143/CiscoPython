def outerfunc(x,y):
    def innerfunc(x,y):
        return str(x)+str(y)
    z=innerfunc(x,y)+"Developers"
    return z
print(outerfunc("Emma","Kelly"))