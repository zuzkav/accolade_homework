import unittest

from missing_integer import solution


class MissingIntTest(unittest.TestCase):
    def test_all_negative(self):
        self.assertEqual(solution([-1, -3]), 1)

    def test_unsorted(self):
        self.assertEqual(solution([1, 3, 6, 4, 1, 2]), 5)

    def test_sorted(self):
        self.assertEqual(solution([1, 2, 3]), 4)

    def test_mixed(self):
        self.assertEqual(solution([1, 2, -3, -50, 0, -1, 4, 5]), 3)

    def test_big_array(self):
        array = [i for i in range(1000) if i != 105]
        self.assertEqual(solution(array), 105)


if __name__ == "__main__":
    unittest.main()
