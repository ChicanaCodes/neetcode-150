def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Given an array of strings, group the anagrams together
    and return a 2D array of the grouped anagrams.

    Example:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

    Edge Cases: 
    - Can there be an empty string?
    - Can there be strings with only one character?
    - Can there be the same string repeated?
    - Can there be null strings?
    - Can the strings have trailing spaces?
    - What to return if there are no anagrams?

    Approach:
    - Create a dictionarty to store the anagrams
    - Iterate through the strings and sort the characters in each string
    - If the sorted string is not in the dictionary, add it as a key and the original string as a value
    - If the sorted string is in the dictionary, add the original string to the value list
    - Return the values of the dictionary as a list of lists

    >>> group_anagrams(["eat","tea","tan","ate","nat","bat"])
    [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]

    >>> group_anagrams(["x"])
    [['x']]

    >>> group_anagrams(["",""])
    [['', '']]

    >>> group_anagrams(["act","pots","tops","cat","stop","hat"])
    [['act', 'cat'], ['hat'], ['pots', 'stop', 'tops']]

    Sample anagrams for following input: ["eat","tea","tan","ate","nat","bat"]
    {
        "aet": ["eat","tea","ate"],
        "ant": ["tan","nat"],
        "abt": ["bat"]
    }
    """
    anagrams = {}
    for string in strs:
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams: 
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]

    # Sort each group and then sort the list of groups for consistent output
    result = [sorted(group) for group in anagrams.values()]
    result.sort()
    return result

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n** ALL TESTS PASSED. AWESOME WORK! **\n")