import random
import sys
import math

if __name__ == "__main__":
    assert (len(sys.argv) - 2) == 4 # without script name and points count
    random.seed(42)

    points = []

    clusters_count = 2
    points_count = int(sys.argv[1])

    for i in range(clusters_count):
        r1, r2 = float(sys.argv[2 + i * 2]), float(sys.argv[2 + i * 2 + 1])
        assert r1 < r2
        for _ in range(points_count):
            phi = random.uniform(0, 2 * math.pi)
            r = random.uniform(r1, r2)
            x = r * math.cos(phi)
            y = r * math.sin(phi)
            points.append((x, y))

    with open('circle_points.txt', 'w') as f:
        for x, y in points:
            f.write('{} {}\n'.format(x, y))
