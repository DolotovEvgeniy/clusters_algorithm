import sys
import random
import math
import copy

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def assign_clusters(points, centers):
    cluster_indx_by_point = {}
    points_by_cluster_indx = {}
    for i in range(len(centers)):
        points_by_cluster_indx[i] = []

    for point in points:
        best_k = 0
        min_distance = distance(point, centers[0])
        for k, center in enumerate(centers):
            cur_distance = distance(point, center)
            if cur_distance < min_distance:
                min_distance = cur_distance
                best_k = k
        cluster_indx_by_point[point] = best_k
        points_by_cluster_indx[best_k].append(point)
    return cluster_indx_by_point, points_by_cluster_indx

def assign_centers(points_by_cluster_indx, centers):
    new_centers = copy.deepcopy(centers)
    for i in range(len(new_centers)):
        points_count = len(points_by_cluster_indx[i])
        if points_count == 0:
            continue
        center_x = sum(x for x, y in points_by_cluster_indx[i]) / float(points_count)
        center_y = sum(y for x, y in points_by_cluster_indx[i]) / float(points_count)
        new_centers[i] = (center_x, center_y)
    return new_centers

def main():
    points = []
    for line in open(sys.argv[1]):
        x, y = map(float, line.strip().split())
        points.append((x, y))
    k = int(sys.argv[2])

    centers = random.sample(points, k)

    cluster_indx_by_point, points_by_cluster_indx = assign_clusters(points, centers)

    while True:
        new_centers = assign_centers(points_by_cluster_indx, centers)
        new_cluster_indx_by_point, new_points_by_cluster_indx = assign_clusters(points, new_centers)
        if new_cluster_indx_by_point == cluster_indx_by_point:
            break
        cluster_indx_by_point, points_by_cluster_indx = new_cluster_indx_by_point, new_points_by_cluster_indx
    with open('clusters.txt', 'w') as f:
        for point, cluster_indx in cluster_indx_by_point.items():
            f.write('{} {} {}\n'.format(point[0], point[1], cluster_indx))

if __name__ == "__main__":
    main()
