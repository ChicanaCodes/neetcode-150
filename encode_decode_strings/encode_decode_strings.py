def encode(strings: list[str]) -> str:
    """
    Takes in a list of strings and transforms it into a single string.
    
    Inout: ['hello', 'world']
    Output: 'helloworld' ?

    Edge Cases: 
    - Can the list be empty?
    - Can the strings be empty?
    - Can the strings contain special characters?
    - Can the strings contain spaces?
    - Can the strings contain numbers?
    - Can the strings be of different lengths?
    - Can the list contain null values?
    - Can the list contain duplicate strings?
    - Can the strings be of the same length or value? 

    Example:
    encode(['hello', 'world']) -> 5#hello5#world
    Approach: 
    1. Iterate over the list of strings and encode each string by prepending its length followed by a '#' character.
       For example, 'hello' becomes '5#hello' and 'world' becomes '5#world'.
       Concatenate these encoded strings together with a separator (e.g., '_').
       So, the final encoded string would be '5#hello5#world'.
    2. Return the encoded string.

    >>> encode(['hello', 'world'])
    '5#hello5#world'

    >>> encode(['a', 'b', 'c'])
    '1#a1#b1#c'

    >>> encode([])
    ''

    >>> encode(['', ''])
    '0#0#'
    
    """
    encoded_string = ''
    for string in strings:
        encoded_string += f"{len(string)}#{string}"
    return encoded_string

def decode(string: str) -> list[str]:
    """
    Takes in a string and transforms it into a list strings
    >>> decode('5#hello5#world')
    ['hello', 'world']

    >>> decode('1#a1#b1#c')
    ['a', 'b', 'c']

    >>> decode('')
    []

    >>> decode('0#0#')
    ['', '']
    
    """
    strs = []
    i = 0
    while i < len(string):
        j = i
        while string[j] != '#':
            j += 1 # Find the end of the encoded string
        length = int(string[i:j]) # Get the length of the encoded string
        strs.append(string[j+1:j+1+length]) # Decode the string and append it to the list of strings
        i = j + 1 + length # Move to the next encoded string
    return strs

if __name__ == '__main__':
    import doctest
    
    doctest.testmod().failed == 0, print("All tests passed.")
    # print(encode(["hello", "world"]))
    # print(decode("5#hello5#world"))