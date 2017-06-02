import timeit

timeit.timeit('"-".join(str(n) for n in range(100))', number=1000)
