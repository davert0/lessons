from exponentiation import exponentiate
import pytest


@pytest.mark.parametrize(
    "n,m,expected", [(4, 6, 4**6), (2, 7, 2**7), (9, 4, 9**4)]
)
def test_exponentiate_normal_value(n, m, expected):
    assert exponentiate(n, m) == expected


@pytest.mark.parametrize(
    "n,m,expected", [(4, 0, 1), (2, 0, 1), (9, 0, 1), (0, 0, 1), (1, 0, 1)]
)
def test_exponentiate_zero(n, m, expected):
    assert exponentiate(n, m) == expected


@pytest.mark.parametrize(
    "n,m,expected", [(4, 1, 4), (2, 1, 2), (9, 1, 9), (0, 1, 0), (1, 1, 1)]
)
def test_exponentiate_one(n, m, expected):
    assert exponentiate(n, m) == expected
