from scipy.spatial import distance

def dist(u, v):
    return round(distance.chebyshev(u, v), 2)