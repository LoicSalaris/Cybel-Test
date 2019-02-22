from string import ascii_letters

def palindrome(candidate):
    """
    Returns True if candidate is a palindrome, ignoring whitespaces and punctuation.
    """
    stripped = [char.lower() for char in candidate if char in ascii_letters]
    return stripped == stripped[::-1]

print (palindrome("Elu par cette crapule"))

print (palindrome("Was it a rat I saw?"))
