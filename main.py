from test_cases import test_has_unique_characters
from solutions import has_unique_characters_set,has_unique_characters_sort, has_unique_characters_brute_force

if __name__ == "__main__":
    test_has_unique_characters(has_unique_characters_set)
    test_has_unique_characters(has_unique_characters_sort)
    test_has_unique_characters(has_unique_characters_brute_force)
    