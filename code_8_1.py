# Write a method to generate the nth Fibonacci number.
def fibo(n):
    assert n>=0
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        a=1
        b=1
        c=0
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
        return c
if __name__ == '__main__':
    print(fibo(4))


