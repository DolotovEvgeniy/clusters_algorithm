import cv2
import sys
import numpy as np
import random

WIDTH = 500
HEIGHT = 500
PAD = 100

def main():
    points = []
    with open(sys.argv[1]) as f:
        for line in f:
            x, y, k = line.strip().split()
            x, y = float(x), float(y)
            k = int(k)
            points.append((x, y, k))

    min_x = points[0][0]
    max_x = points[0][0]
    min_y = points[0][1]
    max_y = points[0][1]
    max_k = 0
    for x, y, k in points:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        max_k = max(max_k, k)

    color_by_k = {}
    for i in range(max_k + 1):
        color_by_k[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    ratio = min(WIDTH / (max_x - min_x), HEIGHT / (max_y - min_y))
    mean_x = (max_x - min_x) / 2
    mean_y = (max_y - min_y) / 2

    image = np.ones([HEIGHT + 2 * PAD, WIDTH + 2 * PAD, 3], dtype=np.uint8) * 255
    for x, y, k in points:
        x = (x - min_x) * ratio + PAD
        y = (y - min_y) * ratio + PAD
        cv2.circle(image, (int(x), int(y)), 5, color_by_k[k], -1)
    cv2.imwrite("clusters.png", image)

if __name__ == "__main__":
    main()
