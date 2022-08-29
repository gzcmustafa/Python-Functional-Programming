from re import I


def kareAl(n):
    i=1
    while i<n:
        yield i*i
        i+=1
    else:
        raise StopIteration

y=kareAl(5)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

