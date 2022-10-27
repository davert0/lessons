from palindrome import is_palindrome


def test_is_palindrome():
    palindromes = [
            "Poor Dan is in a droop.",
            "Sit on a potato pan, Otis.",
            "noon",
            "civic",
            "racecar",
            "level",
            "No lemon, no melon",
            "Mr. Owl ate my metal worm.",
        ]
    for palindrome in palindromes:
        assert is_palindrome(palindrome) == True
    
    assert is_palindrome("fsad") == False
    assert is_palindrome("nice to meet you") == False
    assert is_palindrome("nice to meet yon") == False