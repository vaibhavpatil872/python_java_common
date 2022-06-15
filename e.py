print("hello")
n=5
for i in range(n):
    print(' '*(n-i-1)+("*"+' ')*(i+1))
for j in range(n):
    print(' '*(j+1)+("*"+' ')*(n-j-1))
    