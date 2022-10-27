import pytest
from list_length import get_list_length


@pytest.mark.parametrize("input,expected", [([1, 2, 3], 3), ([1, 1, 1, 1], 4), ([], 0)])
def test_list_length(input, expected):
    assert get_list_length(input) == expected
