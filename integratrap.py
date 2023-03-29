import math
import multiprocessing as mp
from time import perf_counter

def integra_trap(func, a, b, num):
    dx = (a + b) / num
    res = 0
    for i in range(num):
        res += ((func(dx * i) + func(dx * (i + 1))) / 2) * dx
    return res

def integra_trap_paral(func, a, b, num, q):
    dx = (a + b) / num
    res = 0
    for i in range(num):
        res += ((func(dx * i) + func(dx * (i + 1))) / 2) * dx
    q.put(res)

f = lambda x: x*math.sin(math.cos(x)) + (x ** 0.5)

n = mp.cpu_count()
procs = []
q = mp.Queue()
s = perf_counter()
for i in range(n):
    p = mp.Process(target=integra_trap_paral, args=(f, 0 + i*(100 / n), 0 + (i + 1)*(10000 / n), 60000, q))
    procs.append(p)
    p.start()
    
for i in procs:
    i.join()

I = 0
while not q.empty():
    I += q.get()
    
e = perf_counter()
print(e - s, 'p')

s = perf_counter()
I2 = integra_trap(func, 0, 100000, 480000)
e = perf_counter()

print(e - s, 'not p')