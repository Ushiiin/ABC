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

#和のセグ木にするときは以下の関数を定義する必要あり。
def segfunc(x,y):
  return x+y

class SegmentTree(object):
    def __init__(self, A, dot, unit):
        n = 1 << (len(A) - 1).bit_length()
        tree = [unit] * (2 * n)
        for i, v in enumerate(A):
            tree[i + n] = v
        for i in range(n - 1, 0, -1):
            tree[i] = dot(tree[i << 1], tree[i << 1 | 1])
        self._n = n
        self._tree = tree
        self._dot = dot
        self._unit = unit

    def __getitem__(self, i):
        return self._tree[i + self._n]

    def update(self, i, v):
        i += self._n
        self._tree[i] = v
        while i != 1:
            i >>= 1
            self._tree[i] = self._dot(self._tree[i << 1], self._tree[i << 1 | 1])

    def add(self, i, v):
        self.update(i, self[i] + v)

    def sum(self, l, r): #これで[l,r)から取り出す。
        l += self._n
        r += self._n
        l_val = r_val = self._unit
        while l < r:
            if l & 1:
                l_val = self._dot(l_val, self._tree[l])
                l += 1
            if r & 1:
                r -= 1
                r_val = self._dot(self._tree[r], r_val)
            l >>= 1
            r >>= 1
        return self._dot(l_val, r_val)


def main():
    N,X,Y = map(int,input().split()); INF = pow(10,9)
    A = list(map(int,input().split()))
    NG = deque([]); MAX = deque([]); MIN = deque([])
    for i,a in enumerate(A):
        if a < Y or a > X:
            NG.append(i)
        if a == X:
            MAX.append(i)
        if a == Y:
            MIN.append(i)
    NG.append(N)

    ans = 0
    for l in range(N):
        r = NG[0]
        #[l,r)
        if not MAX or not MIN: break
        req = max(MAX[0], MIN[0])
        #print(l,r,req)
        #req以上、r未満
        ans += max(0, r - req)
        if NG[0] == l:
            NG.popleft()
        if MAX[0] == l:
            MAX.popleft()
        if MIN[0] == l:
            MIN.popleft()
    print(ans)


if __name__ == '__main__':
    main()