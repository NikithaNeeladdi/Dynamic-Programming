#Basic implementation of Fibonacci using recursion 

def fib(n:int):
    if n == 0 :
        return 1
    if n == 1:
        return 1
    return fib(n-1)+ fib(n-2)

if __name__ == '__main__':
    import timeit
    
    for n in [10,20,30]:
        duration = timeit.timeit('fib(n)',number=100,globals=globals())
        print(n,"took",duration,"to run")
    