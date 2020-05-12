from scipy.spatial import distance

def dist(u, v):
    return round(distance.cityblock(u, v), 2)
