def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Given a list of integers, return the values that are repeated the most in the list. 
    if k = 1, return the value that appears most frequently.
    if k = 2, return the two values that appear most frequently.
    etc.

    Input: nums = [1, 2, 3, 3, 4], k = 1
    Output:  [3]

    Input: nums = [5, 5, 5, 4, 4, 4, 3], k = 2
    Output: [4, 5]

    Edge Cases: 
    - Can all the values only appear once? 
    - Can you have negative numbers in the list?
    - Can multiple numbers appear the same amount of times?
    - Can the list be empty?
    - Is the array sorted in any order?
    - Can the k value be greater than the number of unique values in the list?
    - Can the k value be negative?
    - Can the k value be 0?

    Approach: 
    1. Create an hashtable to store the frequencey of each number
    2. Iterate over the hashtable and keep track of the the k most frequent numbers
    3. Return the k most frequent numbers

    Example: 
    nums = [1, 2, 3, 3, 4], k = 1
    hash_table = {1: 1, 2: 1, 3: 2, 4: 1}
    result = [3]

    >>> top_k_frequent([7, 7], 1)
    [7]
    
    >>> top_k_frequent([1,2,2,3,3,3], 2)
    [2, 3]
    """

    values_frequency = {}
    for num in nums:
        values_frequency[num] = 1 + values_frequency.get(num, 0)
    print(values_frequency)  # Debugging line to see the frequency count
    value_counts = []
    for num, count in values_frequency.items():
        value_counts.append([count, num])
    value_counts.sort() # O (n log n)

    print(value_counts)
    k_most_frequent = []
    while len(k_most_frequent) < k:
        k_most_frequent.append(value_counts.pop()[1])
    return k_most_frequent

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod().failed == 0, "All doctests passed."
    

print(top_k_frequent([1, 2, 3, 3, 3, 3, 4, 4, 4], 2))  # Output: [3]