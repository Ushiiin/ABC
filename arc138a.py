from re import L
import sys
#input = sys.stdin.readline
input = sys.stdin.buffer.readline #文字列はダメ
#sys.setrecursionlimit(1000000)
#import bisect
#import itertools
#import random
#from heapq import heapify, heappop, heappush
#from collections import defaultdict 
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
    N,K = map(int,input().split()); INF = pow(10,9) + 10
    A = list(map(int,input().split()))

    AK = [INF]
    for i in reversed(range(K)):
        AK.append(min(AK[-1], A[i]))
    AK.reverse()
    #print(AK)
    ans = INF
    for i in range(K,N):
        if A[K-1] < A[i]:
            temp = i - (K-1)
            ans = min(ans, temp)
            continue
        if AK[0] >= A[i]:
            continue

        ok = 0
        ng = K
        while abs(ok-ng) > 1:
            mid = (ok+ng)//2
            if A[i] > AK[mid]:
                ok = mid
            else:
                ng = mid
        #print("i",i,"ok",ok)
        #print(A[i])
        #print(AK[ok])
        temp = i - ok
        ans = min(ans, temp)
    if ans == INF:
        print(-1)
    else:
        print(ans)
    #print(ans)
    





if __name__ == '__main__':
    main()