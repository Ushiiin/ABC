import sys
#input = sys.stdin.readline
#input = sys.stdin.buffer.readline #文字列はダメ
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
MOD = 998244353
#dx = [1,0,-1,0]
#dy = [0,1,0,-1]
#dx8 = [1,1,0,-1,-1,-1,0,1]
#dy8 = [0,1,1,1,0,-1,-1,-1]
#dx = [1,1,-1,-1]
#dy = [1,-1,1,-1]

class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]
    def find(self, x):
        """
        x が属するグループを探索して親を出す。
        """
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def union(self, x, y):
        """
        x と y のグループを結合
        """
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]
    def is_same(self, x, y):
        """
        x と y が同じグループか否か
        """
        return self.find(x) == self.find(y)
    def get_size(self, x):
        """
        x が属するグループの要素数
        """
        x = self.find(x)
        return self.size[x]


def main():
    N = int(input())
    P = list(map(int,input().split()))
    P = [p-1 for p in P]
    Q = list(map(int,input().split()))
    Q = [q-1 for q in Q]

    uf = UnionFind(N)
    for p,q in zip(P,Q):
        uf.union(p,q)
    
    ans = 1
    used = set([])
    for i in range(N):
        par = uf.find(i)
        if par in used: continue
        used.add(par)

        M = uf.get_size(par)
        #M = 4
        #print(M)
        #1本目が使われない
        #dp:0/1:0は次が入っている、１は入っていない
        dp = [1,0]
        for j in range(M-1):
            p = [0,0]
            p,dp = dp,p
            dp[1] += p[0] #次の辺を選ばない
            dp[0] += p[1] + p[0] #次の辺を選ぶ
            dp[1] %= MOD
            dp[0] %= MOD
            #print(dp)
        temp = dp[0] + dp[1]
        #print("Q")
        dp = [0,1]
        for j in range(M-1):
            p = [0,0]
            p,dp = dp,p
            dp[1] += p[0] #次の辺を選ばない
            dp[0] += p[1] + p[0] #次の辺を選ぶ
            dp[1] %= MOD
            dp[0] %= MOD
            #print(dp)
        temp += dp[0]
        temp %= MOD
        ans *= temp
        ans %= MOD
    print(ans%MOD)





if __name__ == '__main__':
    main()