import unittest
import time

import numpy as np


def edist(a, b):
    return np.sqrt(np.sum((a - b)**2))


def brute_force_closest_pair(points):
    mind = 1e9
    ans = (None, None)
    for i, point in enumerate(points):
        for neighbor in points[i + 1:]:
            d = edist(point, neighbor)
            if d < mind:
                ans = (point, neighbor)
                mind = d
    return ans, mind



def closest_split_pair(Px, Py, delta):
    xbar = Px[int(len(Px) / 2)][0]
    xleft = xbar - delta
    xright = xbar + delta
    Sy = np.array([p for p in Py if xleft <= p[0] <= xright])
    mind = delta + 1
    ans = (None, None)
    for i, point in enumerate(Sy[:-1]):
        for j in range(1, min(8, len(Sy) - i)):
            d = edist(point, Sy[i + j])
            if d < mind:
                ans = (point, Sy[i + j])
                mind = d
    return ans, mind


def closest_pair_same(Px, Py):
    if len(Px) < 4:
        return brute_force_closest_pair(Px)
    else:
        midx = Px[int(len(Px) / 2)][0]
        Qx = np.array([p for p in Px if p[0] < midx])
        Rx = np.array([p for p in Px if p[0] >= midx])
        Qy = np.array([p for p in Py if p[0] < midx])
        Ry = np.array([p for p in Py if p[0] >= midx])
        (p1, q1), dx = closest_pair_same(Qx, Qy)
        (p2, q2), dy = closest_pair_same(Rx, Ry)
        (p3, q3), ds = closest_split_pair(Px, Py, min(dx, dy))
        mind = min(dx, dy, ds)
        if mind == dx:
            return (p1, q1), dx
        elif mind == dy:
            return (p2, q2), dy
        else:
            return (p3, q3), ds


def closest_pair(points):
    Px = np.array(sorted(points, key=lambda p: p[0]))
    Py = np.array(sorted(points, key=lambda p: p[1]))
    return closest_pair_same(Px, Py)


class TestClosestPair(unittest.TestCase):

    def test_closest_pair(self):
        points = 10 * np.random.random(size=(1000, 2))
        start = time.time()
        (p1, p2), d1 = brute_force_closest_pair(points)
        brute_time = time.time() - start
        start = time.time()
        (q1, q2), d2 = closest_pair(points)
        div_time = time.time() - start
        self.assertTrue((np.all(p1 == q1) and np.all(p2 == q2)) or
                        (np.all(p1 == q2) and np.all(p2 == q1)))
        self.assertTrue(d1 == d2)
        self.assertTrue(div_time < brute_time)


if __name__ == '__main__':
    unittest.main()
