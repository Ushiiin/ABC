import sys
#input = sys.stdin.readline
#input = sys.stdin.buffer.readline #文字列はダメ
#sys.setrecursionlimit(1000000)
#import bisect
#import itertools
#import random
#from heapq import heapify, heappop, heappush
from collections import defaultdict 
#from collections import deque
#import copy
#import math
#from functools import lru_cache
#@lru_cache(maxsize=None)
#MOD = pow(10,9) + 7
#MOD = 998244353
#dx = [1,0,-1,0]
#dy = [0,1,0,-1]
#dx8 = [1,1,0,-1,-1,-1,0,1]
#dy8 = [0,1,1,1,0,-1,-1,-1]
#dx = [1,1,-1,-1]
#dy = [1,-1,1,-1]

def main():
    N = int(input())
    nick = defaultdict(int)
    name = []
    for i in range(N):
        s,t = map(str,input().split())
        name.append((s,t))
        if s == t:
            nick[s] += 1
        else:
            nick[s] += 1
            nick[t] += 1
    
    for s,t in name:
        if nick[s] >= 2 and nick[t] >= 2:
            print('No');exit()
    print('Yes')


if __name__ == '__main__':
    main()