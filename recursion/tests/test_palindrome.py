from palindrome import is_palindrome


def test_is_palindrome():
    palindromes = [
        "poordanisinadroop",
        "sitonapotatopanotis",
        "noon",
        "civic",
        "racecar",
        "level",
        "nolemonnomelon",
        "mrowlatemymetalworm",
    ]
    for palindrome in palindromes:
        assert is_palindrome(palindrome) == True

    assert is_palindrome("fsad") == False
    assert is_palindrome("nice to meet you") == False
    assert is_palindrome("nice to meet yon") == False
