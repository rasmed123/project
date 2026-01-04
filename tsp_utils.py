import random
import math
import itertools

def generate_instance(n, seed=0):
    random.seed(seed)
    return [(random.random(), random.random()) for _ in range(n)]

def euclidean(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def distance_matrix(coords):
    n = len(coords)
    dist = [[euclidean(coords[i], coords[j]) for j in range(n)] for i in range(n)]
    return dist

def tour_length(tour, dist):
    return sum(dist[tour[i]][tour[(i+1) % len(tour)]] for i in range(len(tour)))

def exact_tsp(dist):
    n = len(dist)
    best = float("inf")
    for perm in itertools.permutations(range(n)):
        best = min(best, tour_length(perm, dist))
    return best
