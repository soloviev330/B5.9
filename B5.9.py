

def time_this(iters):
    def decorator(func):
        def wrapper(*args, **kwargs):
            import time
            total = 0
            for n in range(iters):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print("Общее время выполнения: %.5f секунд" % (total))
        return wrapper

    return decorator

@time_this(iters=2000)
def fibo():
    fibo = []
    fibo_limit = 40000000000000000000000000000000000000000000000000000
    a=1
    i=0
    while a < fibo_limit:
        a += i
        if a < fibo_limit:
            fibo.append(a)
            i=fibo[len(fibo)-2]

    _sum = 0
    for number in fibo:
        if number % 2 == 0:
            _sum += number


fibo()
