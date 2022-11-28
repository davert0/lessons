from generate_bst_arr import GenerateBBSTArray
import random


def test_generate_bst_arr():
    input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    expected = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    for i in range(10):
        random.shuffle(input)
        assert GenerateBBSTArray(input) == expected
