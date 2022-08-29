from re import A


def test(a):
    a+=1
    yield a

    a+=1
    yield a

x=test(5)
print(next(x))
print(next(x))
#hata verecek print(next(x))