from scoop import futures
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

if __name__ == "__main__":
  futures.map(harmonic, range(1600000))

print(time.localtime())
