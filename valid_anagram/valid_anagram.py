def is_anagram(s: str, t: str):

    """
    Given 2 strings, check to see if they contain the same number of characters
    Chars can be alphabetic? 
    empty string? 
    None? 
    Case sensitive? is A == a? assume all lowercase
    Special characters? assume no
    Remove white spaces " hello  " vs "hello"

    Input: Two strings
    Output: Boolean

    Pseudocode: 
    1. Sort the strings
    2. Compare them
    3. Return true if equal
    """
    sorted_s = sorted(s)
    sorted_t =sorted(t)
    return sorted_s == sorted_t

s = "racecar"
t = "carrace"
print(is_anagram(s, t))

# Time Complexity - O(n log n) - because sorting
# Space Complexity - O(n)

def is_anagram_counting(s, t):
    char_counts_s = {}
    char_counts_t = {}
    for char in s: 
        if char in char_counts_s:
            char_counts_s[char] = char_counts_s[char] + 1
        else: 
            char_counts_s[char] = 1
    for char in t: 
        if char in char_counts_t:
            char_counts_t[char] = char_counts_t[char] + 1
        else: 
            char_counts_t[char] = 1

    return char_counts_s == char_counts_t

print(is_angagram_counting(s, t))

# Time Complexity - O(n)
# Space Complexity - O(n)

from collections import Counter

def is_anagram_counter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

print(is_anagram_counter(s, t))

# Time Complexity - O(n)
# Space Complexity - O(n)

def is_anagram_optimized(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    char_count = {}
    
    # Count characters in s
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Decrement counts for characters in t
    for char in t:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    
    return True

print(is_anagram_optimized(s, t))

# Time Complexity - O(n)
# Space Complexity - O(n)




    