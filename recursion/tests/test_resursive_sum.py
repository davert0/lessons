import pytest
from sum import recursive_sum

@pytest.mark.parametrize(
    "input,expected", 
    [
        (12345, 15),
        (5858, 26),
        (0, 0),
        (1, 1),
        (2, 2),
        (45, 9)
    ]
)
def test_recursive_sum(input, expected):
    assert recursive_sum(input) == expected