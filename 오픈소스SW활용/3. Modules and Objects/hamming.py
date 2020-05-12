from scipy.spatial import distance

def dist(u, v):
    return round(distance.hamming(u, v), 2)