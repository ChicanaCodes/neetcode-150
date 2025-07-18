def is_palindrome(s: str) -> bool:
    '''
    Given a string, check whether the same characters exist so that they mirror each other
    hannah => True
    rac e car => True
    banana => False
    Was it a car or a cat I saw? => True
    
    Edge Cases: 
    - Can the string be empty? Yes
    - Can the string have non alphabetic characters? Yes
    - Is the string case sensitive? No
    - Can the string have spaces? Yes
    - Can the string be null? Yes
    - What should we return if the string is empty? True
    - What should we return if the string is null? False
    - What should we return if the string has only non-alphabetic characters? False

    Approach: 
    1. Clean up the string to remove strings and non-alphabetic characters, 
        since we want to ignore non-alphanumeric ones ex. ?, 9, ' ', etc
    2. Mantain 2 pointers, one at the start of the string, one at the end
    3. Check if the characters are the same, if so, move the pointers, left and right
        respectively
    4. If not the same, return False
    5. If the pointers cross each other, return True
    '''
    if s is None:
        return False
    cleaned = ''.join(char.lower() for char in s if char.isalnum()) # O(n) time, O(n) space
    left, right = 0, len(cleaned) - 1
    while left < right: # O(n) time
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True # O(1) time, O(1) space

# Time Complexity: O(n) - We iterate through the string once to clean it up, and then we iterate through the cleaned string once to check for palindrome.
# Space Complexity: O(n) - We create a new string to store the cleaned up version of the input string.
if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("All tests passed!")  