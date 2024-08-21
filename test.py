from solution import has_unique_characters


def test_has_unique_characters():
    # Test Case 1: All unique characters
    assert has_unique_characters("abcdef") == True, "Test Case 1 Failed"
    
    # Test Case 2: Some repeated characters
    assert has_unique_characters("hello") == False, "Test Case 2 Failed"
    
    # Test Case 3: Empty string
    assert has_unique_characters("") == True, "Test Case 3 Failed"
    
    # Test Case 4: Single character
    assert has_unique_characters("a") == True, "Test Case 4 Failed"
    
    # Test Case 5: String with all same characters
    assert has_unique_characters("aaaaa") == False, "Test Case 5 Failed"
    
    # Test Case 6: Mixed case sensitivity
    assert has_unique_characters("aA") == True, "Test Case 6 Failed"
    
    # Test Case 7: Long string with no duplicates
    assert has_unique_characters("abcdefghijklmnopqrstuvwxyz") == True, "Test Case 7 Failed"
    
    # Test Case 8: Long string with duplicates
    assert has_unique_characters("abcdefghijklmnopqrstuvwxyza") == False, "Test Case 8 Failed"
    
    print("All test cases passed!")