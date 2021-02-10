import random
import sys
import math


if __name__ == "__main__":
    assert (len(sys.argv) - 2) == 8 # without script name and points count
    random.seed(42)

    points = []

    points_count = int(sys.argv[1])

    # cluster 0
    center_x, a = float(sys.argv[2]), float(sys.argv[2 + 1])
    center_y, b = float(sys.argv[2 + 2]), float(sys.argv[2 + 3])
    
    min_v = min(a, b)
    max_v = max(a, b)
    c = math.sqrt(max_v * max_v - min_v * min_v)
    e = c / max_v
    p = min_v * min_v / max_v

    r_epsilon = min(a, b) * 0.15

    for _ in range(points_count):
        phi = random.uniform(-math.pi, 0)
        r = p / (1 - e * math.cos(phi)) + random.uniform(-r_epsilon, r_epsilon)
        x = center_x + r * math.cos(phi)
        y = center_y + r * math.sin(phi)
        points.append((x, y))

    # cluster 1
    center_x, a = float(sys.argv[2 + 4]), float(sys.argv[2 + 4 + 1])
    center_y, b = float(sys.argv[2 + 4 + 2]), float(sys.argv[2 + 4 + 3])
    
    min_v = min(a, b)
    max_v = max(a, b)
    c = math.sqrt(max_v * max_v - min_v * min_v)
    e = c / max_v
    p = min_v * min_v / max_v

    r_epsilon = min(a, b) * 0.15

    for _ in range(points_count):
        phi = random.uniform(0, math.pi)
        r = p / (1 - e * math.cos(phi)) + random.uniform(-r_epsilon, r_epsilon)
        x = center_x + r * math.cos(phi)
        y = center_y + r * math.sin(phi)
        points.append((x, y))

    with open('ellipse_points.txt', 'w') as f:
        for x, y in points:
            f.write('{} {}\n'.format(x, y))
