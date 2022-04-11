import sys
#input = sys.stdin.readline
#input = sys.stdin.buffer.readline #文字列はダメ
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
    Query = int(input())
    #xがc個
    Q = deque([])
    for _ in range(Query):
        query = input().split()
        #print(Q)
        if query[0] == "1":
            x = int(query[1])
            c = int(query[2])
            if Q and Q[-1][0] == x:
                Q[-1][1] += c
            else:
                Q.append([x,c])
        else:
            c = int(query[1])
            ans = 0
            while c > 0:
                if Q[0][1] <= c:
                    px,pc = Q.popleft()
                    ans += px*pc
                    c -= pc
                else:
                    Q[0][1] -= c
                    px = Q[0][0]
                    ans += px*c
                    c = 0
            print(ans)



if __name__ == '__main__':
    main()