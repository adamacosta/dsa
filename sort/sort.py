import unittest
import random

import numpy as np


def insertionsort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def merge(a, b):
    len_a = len(a)
    len_b = len(b)
    res = [None] * (len_a + len_b)
    i = 0
    j = 0
    for k, _ in enumerate(res):
        if i > len_a - 1:
            res[k] = b[j]
            j += 1
        elif j > len_b - 1:
            res[k] = a[i]
            i += 1
        elif a[i] < b[j]:
            res[k] = a[i]
            i += 1
        else:
            res[k] = b[j]
            j += 1
    return res


def mergesort(arr):
    len_arr = len(arr)
    if len_arr < 2:
        return arr
    else:
        mid = int(len_arr / 2)
        first = mergesort(arr[:mid])
        second = mergesort(arr[mid:])
        return merge(first, second)


def partition(arr, idx):
    arr[idx], arr[0] = arr[0], arr[idx]
    pivot = arr[0]
    i = 1
    for j in range(1, len(arr)):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i - 1], arr[0] = arr[0], arr[i - 1]
    return arr, i


def quicksort(arr):
    if len(arr) < 10:
        return insertionsort(arr)
    else:
        idx = random.randint(0, len(arr) - 1)
        arr, pidx = partition(arr, idx)
        arr[:pidx] = quicksort(arr[:pidx])
        arr[pidx:] = quicksort(arr[pidx:])
        return arr


class TestSort(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.small_arr = np.random.random_integers(100, size=100)
        cls.big_arr = np.random.random_integers(int(1e5), size=int(1e5))
        cls.small_sorted = np.sort(cls.small_arr)
        cls.big_sorted = np.sort(cls.big_arr)

    def test_insertionsort(self):
        self.assertTrue(
            np.all(self.small_sorted == insertionsort(self.small_arr))
        )

    def test_mergesort(self):
        self.assertTrue(
            np.all(self.big_sorted == mergesort(self.big_arr))
        )

    def test_quicksort(self):
        self.assertTrue(
            np.all(self.big_sorted == quicksort(self.big_arr))
        )


if __name__ == '__main__':
    unittest.main()
