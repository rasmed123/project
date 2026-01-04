import random
import math
import time

class SA:
    def __init__(self, dist, T0=1000, alpha=0.995, iters=100):
        self.dist = dist
        self.n = len(dist)
        self.T0 = T0
        self.alpha = alpha
        self.iters = iters

    def _length(self, t):
        return sum(self.dist[t[i]][t[(i+1)%self.n]] for i in range(self.n))

    def _neighbor(self, t):
        a,b = sorted(random.sample(range(self.n),2))
        t2 = t[:]
        t2[a:b] = reversed(t2[a:b])
        return t2

    def run(self):
        t = list(range(self.n))
        random.shuffle(t)
        best = t[:]
        best_len = self._length(t)
        T = self.T0
        start = time.time()

        while T > 1e-3:
            for _ in range(self.iters):
                n = self._neighbor(t)
                d = self._length(n) - self._length(t)
                if d < 0 or random.random() < math.exp(-d/T):
                    t = n
                    if self._length(t) < best_len:
                        best, best_len = t[:], self._length(t)
            T *= self.alpha

        return best, best_len, time.time()-start
