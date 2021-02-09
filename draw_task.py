import cv2
import sys
import numpy as np

WIDTH = 500
HEIGHT = 500
PAD = 100

def main():
    points = []
    with open(sys.argv[1]) as f:
        for line in f:
            x, y = map(float, line.strip().split())
            points.append((x, y))

    min_x = points[0][0]
    max_x = points[0][0]
    min_y = points[0][1]
    max_y = points[0][1]
    for x, y in points:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)


    ratio = min(WIDTH / (max_x - min_x), HEIGHT / (max_y - min_y))
    mean_x = (max_x - min_x) / 2
    mean_y = (max_y - min_y) / 2

    image = np.ones([HEIGHT + 2 * PAD, WIDTH + 2 * PAD], dtype=np.uint8) * 255
    for x, y in points:
        x = (x - min_x) * ratio + PAD
        y = (y - min_y) * ratio + PAD
        cv2.circle(image, (int(x), int(y)), 5, 0, -1)
    cv2.imwrite("task.png", image)

if __name__ == "__main__":
    main()
