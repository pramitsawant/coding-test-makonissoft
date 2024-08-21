def has_unique_characters(s: str) -> bool:
    """
    Determines if a string has all unique characters using a Set.
    
    Algorithm: Iterate through the string and use a set to keep track of characters we've seen. If a character is already in the set, the string doesn't have all unique characters.

    Time Complexity: O(n), where n is the length of the string.
    Space Complexity: O(n) due to the set.    

    :param s: The input string to check.
    :return: True if all characters in the string are unique, False otherwise.
    """
    # Using a set to track unique characters
    seen_chars = set()
    
    for char in s:
        if char in seen_chars:
            return False
        seen_chars.add(char)
    
    return True