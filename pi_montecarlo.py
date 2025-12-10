import random
import time

i = 1
print('#p\ttime')
while i <= 8: # i should be less than 9
    tic = time.time()
    n = 10**i
    x = [random.random() for _ in range(n)]
    y = [random.random() for _ in range(n)]
    int_points = [d for d in range(n) if (x[d]**2+y[d]**2)**0.5 < 1]
    toc = time.time()
    print(f'10^{i}\t{round(toc-tic, 3)} \t-> π = {4*len(int_points)/n}')
    i += 1
