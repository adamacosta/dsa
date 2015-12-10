import unittest
import time

import numpy as np


def brute_inversion_count(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count


def count_split(a, b):
    len_a = len(a)
    len_b = len(b)
    res = [None] * (len_a + len_b)
    i = 0
    j = 0
    count = 0
    for k, _ in enumerate(res):
        if i > len_a - 1:
            res[k] = b[j]
            j += 1
        elif j > len_b - 1:
            res[k] = a[i]
            i += 1
        elif a[i] <= b[j]:
            res[k] = a[i]
            i += 1
        else:
            res[k] = b[j]
            j += 1
            count += len_a - i
    return count, res


def inversion_count(arr):
    if len(arr) == 1:
        return 0, arr
    else:
        mid = int(len(arr) / 2)
        count_left, arr_left = inversion_count(arr[:mid])
        count_right, arr_right = inversion_count(arr[mid:])
        count, sorted_arr = count_split(arr_left, arr_right)
        return count_left + count_right + count, sorted_arr


class TestInversion(unittest.TestCase):

    def test_inversion_count(self):
        rand_arr = np.random.permutation(np.arange(1, 1001))
        start = time.time()
        brute_count = brute_inversion_count(rand_arr)
        brute_time = time.time() - start
        start = time.time()
        div_count, trash = inversion_count(rand_arr)
        div_time = time.time() - start
        self.assertTrue(brute_count == div_count)
        self.assertTrue(div_time < brute_time)


if __name__ == '__main__':
    unittest.main()
