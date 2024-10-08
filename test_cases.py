def test_has_unique_characters(func):
    # Test Case 1: All unique characters
    assert func("abcdef") == True, "Test Case 1 Failed"
    
    # Test Case 2: Some repeated characters
    assert func("hello") == False, "Test Case 2 Failed"
    
    # Test Case 3: Empty string
    assert func("") == True, "Test Case 3 Failed"
    
    # Test Case 4: Single character
    assert func("a") == True, "Test Case 4 Failed"
    
    # Test Case 5: String with all same characters
    assert func("aaaaa") == False, "Test Case 5 Failed"
    
    # Test Case 6: Mixed case sensitivity
    assert func("aA") == True, "Test Case 6 Failed"
    
    # Test Case 7: Long string with no duplicates
    assert func("abcdefghijklmnopqrstuvwxyz") == True, "Test Case 7 Failed"
    
    # Test Case 8: Long string with duplicates
    assert func("abcdefghijklmnopqrstuvwxyza") == False, "Test Case 8 Failed"
    
    print("All test cases passed!")