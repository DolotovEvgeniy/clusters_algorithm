import sys
from sklearn.cluster import AffinityPropagation
import numpy as np


def main():
    points = []
    for line in open(sys.argv[1]):
        x, y = map(float, line.strip().split())
        points.append((x, y))

    clustering = AffinityPropagation(random_state=5)
    result = clustering.fit_predict(np.array(points))

    with open('clusters.txt', 'w') as f:
        for i, cluster_indx in enumerate(result):
            f.write('{} {} {}\n'.format(points[i][0], points[i][1], cluster_indx))

if __name__ == "__main__":
    main()
