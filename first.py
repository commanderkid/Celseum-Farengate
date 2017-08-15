#c = []
#n = int(input())

#for i in range(0, n):
#    x = int(input())
#    c.append(x)
c = input()
c = c.split(" ")
c = [int(c) for c in c]
c = c[1:]
def m(my):
    p = (my - 32) * (5/9) 
    f = list(str(p))
    if "." in f:
        g = f.index(".")
        g1 = int(f[g+1])
        f1 = f[0:g]
        ff1 = "".join(f1)
    
        if "-" in f:
            if g1 >= 5:
                p = int(ff1) - 1
            else:
                p = int(ff1)
        else:
            if g1 >= 5:
                p = int(ff1) + 1
            else:
                p = int(ff1)
    else:
        p = int(f1)
        
    return p    
pp = list(map(m, c))
pp = [str(pp) for pp in pp]

print(" ".join(pp))
