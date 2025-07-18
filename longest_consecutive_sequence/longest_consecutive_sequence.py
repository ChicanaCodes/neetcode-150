def longest_consecutive(nums:list[int]) -> int:
    '''
    Given a list of integers determine what is the longest sequence of
    numbers in which the numbers are sorted and 1 greater than the previous number.
    The sequence does not need to be contiguous in the list, but the numbers must be
    present in the list.

    Edge Cases:
    - Can the list be empty? Yes, return 0
    - Can the list contain negative numbers? Yes
    - Can the list contain duplicates? Yes
    - Will the list always contain integers? Yes
    - What should we return if there are no consecutive numbers? Return 1
    - What should we return if all the numbers are the same? Return 1
    - What should we return if the list is not sorted? The function should still work
    - What should we return if the list contains only one number? Return 1 

    Approach: 
    1. Convert the list to a set to allow for O(1) lookups.
    2. Iterate through each number in the set.
    3. For each number, check if it is the start of a sequence (i.e., num - 1 is not in the set).
    4. If it is the start of a sequence, iterate through the set to find the length of the sequence.
    5. Keep track of the longest sequence found.
    6. Return the length of the longest sequence.
    >>> longest_consecutive([100, 4, 200, 1, 3, 2])
    4
    >>> longest_consecutive([0,3,7,2,5,8,4,6,0,1])
    9
    >>> longest_consecutive([])
    0
    >>> longest_consecutive([1,2,0,1])
    3
    >>> longest_consecutive([1,1,1,1])
    1
    >>> longest_consecutive([-2,-3,-1,0,1])
    5
    >>> longest_consecutive([10])
    1
    '''
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("All tests passed!")
# Time Complexity: O(n) - We iterate through the list of numbers once to create the set, and then we iterate through the set once to find the longest sequence. Each number is processed at most twice.
# Space Complexity: O(n) - We use a set to store the numbers, which takes up space proportional to the number of unique numbers in the input list.