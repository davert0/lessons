import string


def is_palindrome(text):

    prepared_text = (
        text.lower()
        .replace(" ", "")
        .translate(str.maketrans("", "", string.punctuation))
    )

    if len(prepared_text) <= 1:
        return True

    if prepared_text[0] != prepared_text[-1]:
        return False

    return is_palindrome(prepared_text[1:-1])
