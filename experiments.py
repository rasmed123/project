from tsp_utils import *
from aco import ACO
from sa import SA

def run(n):
    coords = generate_instance(n, seed=42)
    dist = distance_matrix(coords)
    opt = exact_tsp(dist) if n <= 10 else None

    aco = ACO(dist)
    sa = SA(dist)

    _, l1, t1 = aco.run()
    _, l2, t2 = sa.run()

    return opt, (l1, t1), (l2, t2)

if __name__ == "__main__":
    for n in [10, 50, 100]:
        opt, aco_res, sa_res = run(n)
        print(f"n={n}")
        if opt:
            print("Optimal:", opt)
        print("ACO:", aco_res)
        print("SA:", sa_res)
