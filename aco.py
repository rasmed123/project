import random
import time

class ACO:
    def __init__(self, dist, ants=20, alpha=1.0, beta=5.0, rho=0.5, iterations=100):
        self.dist = dist
        self.n = len(dist)
        self.ants = ants
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.iterations = iterations
        self.pheromone = [[1.0]*self.n for _ in range(self.n)]

    def _construct_tour(self):
        tour = [random.randrange(self.n)]
        while len(tour) < self.n:
            i = tour[-1]
            choices = [j for j in range(self.n) if j not in tour]
            weights = [(self.pheromone[i][j]**self.alpha) * ((1/self.dist[i][j])**self.beta) for j in choices]
            s = sum(weights)
            weights = [w/s for w in weights]
            tour.append(random.choices(choices, weights)[0])
        return tour

    def run(self):
        best_len = float("inf")
        best_tour = None
        start = time.time()

        for _ in range(self.iterations):
            tours = []
            for _ in range(self.ants):
                t = self._construct_tour()
                l = sum(self.dist[t[i]][t[(i+1)%self.n]] for i in range(self.n))
                tours.append((t,l))
                if l < best_len:
                    best_len, best_tour = l, t

            for i in range(self.n):
                for j in range(self.n):
                    self.pheromone[i][j] *= (1 - self.rho)

            for t,l in tours:
                for i in range(self.n):
                    a,b = t[i], t[(i+1)%self.n]
                    self.pheromone[a][b] += 1/l
                    self.pheromone[b][a] += 1/l

        return best_tour, best_len, time.time()-start
