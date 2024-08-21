def has_unique_characters_set(s: str) -> bool:
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

def has_unique_characters_sort(string):
    """
    Determines if a string has all unique characters using sorting.
    
    Algorithm: Sort the string and then check for adjacent characters. If any adjacent characters are the same, the string doesn't have all unique characters.

    Time Complexity: O(n log n), due to sorting.
    Space Complexity: O(n) if new sorted string is created or O(1) if sorting is done in place.    
    
    :param s: The input string to check.
    :return: True if all characters in the string are unique, False otherwise.
    """    
    
    sorted_string = sorted(string)
    for i in range(len(sorted_string) - 1):
        if sorted_string[i] == sorted_string[i + 1]:
            return False
    return True

def has_unique_characters_brute_force(string):
    """
    Determines if a string has all unique characters using sorting.
    
    Algorithm: Compare each character with every other character in the string. If any two characters are the same, the string doesn't have all unique characters.
    
    Time Complexity: O(n square) due to the nested loop.
    Space Complexity: O(1) since checking is done in place.    
    
    :param s: The input string to check.
    :return: True if all characters in the string are unique, False otherwise.
    """        
    
    length = len(string)
    for i in range(length):
        for j in range(i + 1, length):
            if string[i] == string[j]:
                return False
    return True