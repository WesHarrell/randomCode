from multiprocessing import Pool 
from mpmath import *
import time

print(time.localtime())

def harmonic(n):
  mp.dns = 25
  mp.pretty = True
  s=0
  for i in arange(1,n):
     s=s+1/i
  return s-log(n)

pool = Pool(processes=24) 

for i in range(1000000):
  pool.apply_async(harmonic, args = (i,))

pool.close() 
pool.join()
print(time.localtime())
