print("hello")
def fibo_gen():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
f1=fibo_gen()
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
    