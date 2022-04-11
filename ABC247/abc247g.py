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

import heapq
 
"""
https://atcoder.jp/contests/practice2/submissions/20653269
"""
 
 
class mcf_graph:
 
    def __init__(self, n):
        self.n = n
        self._edges = []
 
    def add_edge(self, from_, to, cap, cost):
        # assert 0 <= from_ < self.n
        # assert 0 <= to < self.n
        # assert 0 <= cap
        # assert 0 <= cost
        m = len(self._edges)
        self._edges.append(self.__class__.edge(from_, to, cap, 0, cost))
        return m
 
    class edge:
        def __init__(self, from_, to, cap, flow, cost):
            self.from_ = from_
            self.to = to
            self.cap = cap
            self.flow = flow
            self.cost = cost
 
    def get_edge(self, i):
        # assert 0 <= i < len(self._edges)
        return self._edges[i]
 
    def edges(self):
        return self._edges.copy()
 
    def _dual_ref(self, s, t):
        self.dist = [float('inf')] * self.n
        self.vis = [False] * self.n
        self.que_min.clear()
        self.que.clear()
        que_push_que = []
        self.dist[s] = 0
        self.que_min.append(s)
        while self.que_min or self.que or que_push_que:
            if self.que_min:
                v = self.que_min.pop()
            else:
                while que_push_que:
                    heapq.heappush(self.que, que_push_que.pop())
                _, v = heapq.heappop(self.que)
            if self.vis[v]:
                continue
            self.vis[v] = True
            if v == t:
                break
            dual_v = self.dual[v]
            dist_v = self.dist[v]
            for i in range(self.start[v], self.start[v + 1]):
                e = self.elist[i]
                if not e.cap:
                    continue
                cost = e.cost - self.dual[e.to] + dual_v
                if self.dist[e.to] - dist_v > cost:
                    dist_to = dist_v + cost
                    self.dist[e.to] = dist_to
                    self.prev_e[e.to] = e.rev
                    if dist_to == dist_v:
                        self.que_min.append(e.to)
                    else:
                        que_push_que.append((dist_to, e.to))
        if not self.vis[t]:
            return False
 
        for v in range(self.n):
            if not self.vis[v]:
                continue
            self.dual[v] -= self.dist[t] - self.dist[v]
 
        return True
 
    def _csr(self):
        m = len(self._edges)
        self.edge_idx = [0] * m
        redge_idx = [0] * m
        degree = [0] * self.n
        edges = []
        for i, e in enumerate(self._edges):
            self.edge_idx[i] = degree[e.from_]
            degree[e.from_] += 1
            redge_idx[i] = degree[e.to]
            degree[e.to] += 1
            edges.append((e.from_, self.__class__._edge(e.to, -1, e.cap - e.flow, e.cost)))
            edges.append((e.to, self.__class__._edge(e.from_, -1, e.flow, -e.cost)))
        self.start = [0] * (self.n + 1)
        self.elist = [0] * len(edges)
        for v, w in edges:
            self.start[v + 1] += 1
        for i in range(1, self.n + 1):
            self.start[i] += self.start[i-1]
        counter = self.start.copy()
        for v, w in edges:
            self.elist[counter[v]] = w
            counter[v] += 1
        for i, e in enumerate(self._edges):
            self.edge_idx[i] += self.start[e.from_]
            redge_idx[i] += self.start[e.to]
            self.elist[self.edge_idx[i]].rev = redge_idx[i]
            self.elist[redge_idx[i]].rev = self.edge_idx[i]
 
    def slope(self, s, t, flow_limit=float('inf')):
        # assert 0 <= s < self.n
        # assert 0 <= t < self.n
        # assert s != t
 
        self._csr()
 
        self.dual = [0] * self.n
        self.dist = [float('inf')] * self.n
        self.prev_e = [0] * self.n
        self.vis = [False] * self.n
 
        flow = 0
        cost = 0
        prev_cost_per_flow = -1
        result = [(0, 0)]
        self.que = []
        self.que_min = []
        while flow < flow_limit:
            if not self._dual_ref(s, t):
                break
            c = flow_limit - flow
            v = t
            while v != s:
                c = min(c, self.elist[self.elist[self.prev_e[v]].rev].cap)
                v = self.elist[self.prev_e[v]].to
            v = t
            while v != s:
                e = self.elist[self.prev_e[v]]
                e.cap += c
                self.elist[e.rev].cap -= c
                v = self.elist[self.prev_e[v]].to
            d = -self.dual[s]
            flow += c
            cost += c * d
            if prev_cost_per_flow == d:
                result.pop()
            result.append((flow, cost))
            prev_cost_per_flow = d
 
        for i in range(len(self._edges)):
            e = self.elist[self.edge_idx[i]]
            self._edges[i].flow = self._edges[i].cap - e.cap
 
        return result
 
    def flow(self, s, t, flow_limit=float('inf')):
        return self.slope(s, t, flow_limit)[-1]
 
    class _edge:
        def __init__(self, to, rev, cap, cost):
            self.to = to
            self.rev = rev
            self.cap = cap
            self.cost = cost
 
from heapq import heappush, heappop
class MinCostFlow:
    INF = 10**18
 
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]
 
    def add_edge(self, fr, to, cap, cost):
        forward = [to, cap, cost, None]
        backward = forward[3] = [fr, 0, -cost, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)
 
    def flow(self, s, t, f):
        N = self.N; G = self.G
        INF = MinCostFlow.INF
 
        res = 0
        H = [0]*N
        prv_v = [0]*N
        prv_e = [None]*N
 
        d0 = [INF]*N
        dist = [INF]*N
 
        while f:
            dist[:] = d0
            dist[s] = 0
            que = [(0, s)]
 
            while que:
                c, v = heappop(que)
                if dist[v] < c:
                    continue
                r0 = dist[v] + H[v]
                for e in G[v]:
                    w, cap, cost, _ = e
                    if cap > 0 and r0 + cost - H[w] < dist[w]:
                        dist[w] = r = r0 + cost - H[w]
                        prv_v[w] = v; prv_e[w] = e
                        heappush(que, (r, w))
            if dist[t] == INF:
                return None
 
            for i in range(N):
                H[i] += dist[i]
 
            d = f; v = t
            while v != s:
                d = min(d, prv_e[v][1])
                v = prv_v[v]
            f -= d
            res += d * H[t]
            v = t
            while v != s:
                e = prv_e[v]
                e[1] -= d
                e[3][1] += d
                v = prv_v[v]
        return res

def main():
    N = int(input()); INF = pow(10,12)
    MX = 155
    A = []; B = []; C = []
    G = [[-INF]*MX for _ in range(MX)]
    for i in range(N):
        a,b,c = map(int,input().split())
        a -= 1; b -= 1
        #A.append(a)
        #B.append(b)
        #C.append(c)
        #print(a,b,c)
        #辺が上書きされてしまう？
        G[a][b] = max(G[a][b], c)
    #print(G)
    ans = []

    s = 2*MX; t = s + 1
    g = MinCostFlow(2*MX+2)
    for i in range(MX):
        g.add_edge(s,i,1,0)
        g.add_edge(i+MX,t,1,0)
    for a in range(MX):
        for b in range(MX):
            if G[a][b] == -INF: continue
            g.add_edge(a,b+MX,1,INF-G[a][b])
            #print(a,b+MX,1,INF-G[a][b])

    #print(g.edges())
    #for e in g.edges():
    #    print(e.from_,e.to,e.cap,e.cost)

    ans = []
    for i in range(MX):
        F = g.flow(s,t,1)
        #print(F)
        if not F:
            break
        temp = INF - F
        if not ans:
            ans.append(temp)
        else:
            ans.append(ans[-1] + temp)


    print(len(ans))
    for x in ans:
        print(x)





if __name__ == '__main__':
    main()