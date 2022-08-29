def fibGen(n):
    f1,f2=0,1
    i=0
    while i<n:
        f1,f2=f2,f1+f2
        yield f2
        i+=1
    else:
        raise StopIteration

x=fibGen(10)
print(next(x))
print(next(x))
print(next(x))
