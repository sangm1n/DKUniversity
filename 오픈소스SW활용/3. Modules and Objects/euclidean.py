from scipy.spatial import distance

def dist(u, v):
    return round(distance.euclidean(u, v), 2)