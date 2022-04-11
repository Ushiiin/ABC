import sys
#input = sys.stdin.readline
input = sys.stdin.buffer.readline #文字列はダメ
#sys.setrecursionlimit(1000000)
#import bisect
#import itertools
#import random
#from heapq import heapify, heappop, heappush
#from collections import defaultdict 
from collections import deque
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
    A = deque(map(int,input().split()))

    op = 0
    while A:
        if op == 0:
            if A[0] == 1: break
            while A and A[-1] == 0:
                A.pop()
            if not A:
                break
            A.popleft()
            while A and A[-1] == 1:
                A.pop()
            op ^= 1
        else:
            if A[0] == 0: break
            while A and A[-1] == 1:
                A.pop()
            if not A:
                break
            A.popleft()
            while A and A[-1] == 0:
                A.pop()
            op ^= 1
    if A:
        print('No')
    else:
        print('Yes')





if __name__ == '__main__':
    main()