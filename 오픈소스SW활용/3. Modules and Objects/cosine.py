from scipy.spatial import distance

def dist(u, v):
    return round(distance.cosine(u, v), 3)