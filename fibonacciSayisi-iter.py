class Fibo:
    def __iter__(self):
     self.f1=0
     self.f2=1
     return self
    
    def __next__(self):
     self.f1,self.f2=self.f2,self.f1+self.f2
     return self.f2

fibos=Fibo()
x=iter(fibos)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))