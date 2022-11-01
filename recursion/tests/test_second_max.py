import pytest
from second_max import get_second_max


@pytest.mark.parametrize(
    "input,expected",
    [
        ([5, 4, 3, 2, 5], 5),
        ([1, 1], 1),
        ([1, 2], 1),
        ([6, 7, 7], 7),
        ([5, 6, 7], 6),
        ([1, 2, 3, 7, 9, 8], 8),
    ],
)
def test_second_max(input, expected):
    assert get_second_max(input) == expected
