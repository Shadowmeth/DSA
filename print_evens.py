import timeit

def print_evens_till_100():
    evens = []
    for i in range(0, 101):
        if i % 2 == 0:
            evens.append(i)
    return evens

def print_evens_till_100_v2():
    n = 2
    evens = []
    while n <= 100:
        evens.append(n)
        n += 2
    return evens


time_v1 = timeit.timeit('print_evens_till_100()', setup='from __main__ import print_evens_till_100', number=1_000_000)
time_v2 = timeit.timeit('print_evens_till_100_v2()', setup='from __main__ import print_evens_till_100_v2', number=1_000_000)

print(f'Version 1 took {time_v1:.3f} seconds to run')
print(f'Version 2 took {time_v2:.3f} seconds to run')

