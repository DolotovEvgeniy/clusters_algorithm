import random
import sys

def gauss_2d(mu_x, sigma_x, mu_y, sigma_y):
    x = random.gauss(mu_x, sigma_x)
    y = random.gauss(mu_y, sigma_y)
    return (x, y)


if __name__ == "__main__":
    print(len(sys.argv) - 2 % 4)
    assert (len(sys.argv) - 2) % 4 == 0 # without script name and points count
    random.seed(42)

    points = []

    clusters_count = (len(sys.argv) - 2) // 4
    points_count = int(sys.argv[1])

    for i in range(clusters_count):
        mu_x, sigma_x = float(sys.argv[2 + i * 4]), float(sys.argv[2 + i * 4 + 1])
        mu_y, sigma_y = float(sys.argv[2 + i * 4 + 2]), float(sys.argv[2 + i * 4 + 3])
        for _ in range(points_count):
            points.append(gauss_2d(mu_x, sigma_x, mu_y, sigma_y))

    with open('gauss_2d_points.txt', 'w') as f:
        for x, y in points:
            f.write('{} {}\n'.format(x, y))
