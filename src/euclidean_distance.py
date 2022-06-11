"""
Euclidean distance is distance
between two points in Euclidean
space.
"""
import math


def euclidean_distance(p, q):
    assert isinstance(p, tuple) or isinstance(p, list)
    assert len(p) == 2
    assert isinstance(q, tuple) or isinstance(q, list)
    assert len(q) == 2

    euclid_distance = math.sqrt((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2)
    print(euclid_distance)


# Should print 4
euclidean_distance((1, 3), (1, -1))

# Should print 4
euclidean_distance((1, -1), (5, -1))
