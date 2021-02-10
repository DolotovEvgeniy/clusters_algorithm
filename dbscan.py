import sys
import random
import math
import copy
from sklearn.cluster import DBSCAN
import numpy as np

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def get_neighbors(point, points, epsilon):
    neighbors = []
    for other_point in points:
        if distance(point, other_point) <= epsilon:
            neighbors.append(other_point)
    return neighbors

def main():
    points = []
    for i, line in enumerate(open(sys.argv[1])):
        x, y = map(float, line.strip().split())
        points.append((x, y))
    epsilon = float(sys.argv[2])
    m = int(sys.argv[3])

    label = {}
    for point in points:
        label[point] = 'undefined'

    k = 0
    for point in points:
        if label[point] != 'undefined':
            continue
        neighbors = get_neighbors(point, points, epsilon)
        if len(neighbors) < m:
            label[point] = 'noise'
            continue
        k += 1
        label[point] = k
        neighbors.remove(point)
        i = 0
        while i < len(neighbors):
            point_q = neighbors[i]
            if label[point_q] == 'noise':
                label[point_q] = k
            elif label[point_q] != 'undefined':
                pass
            else:
                label[point_q] = k
                neighbors_q = get_neighbors(point_q, points, epsilon)
                if len(neighbors_q) >= m:
                    neighbors += neighbors_q
            i += 1
    with open('clusters.txt', 'w') as f:
        for point, cluster_indx in label.items():
            if cluster_indx == 'noise':
                cluster_indx = -1
            f.write('{} {} {}\n'.format(point[0], point[1], cluster_indx))

if __name__ == "__main__":
    main()
