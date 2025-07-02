def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Given an array of integers and a sum value, return the indices of the two numbers that add up to the sum.

    Example:
    Input: nums = [3,4,5,6], target = 7
    Output: [0,1]

    Edge Cases: 
    - Can values be negative? - Yes
    - Can values be larger than the target? - Yes
    - Can there be duplicates? - Yes
    - Can there be more than one pair that adds up to the target? - Yes, how do we handle this? - We can return all pairs that add up to the target
    - Are the values sorted? - No

    Approach:
    - Hash table approach (for unsorted arrays):
        - Use a hash table to store numbers we've seen and their indices
        - For each number, calculate its complement (target - current_number)
        - If complement exists in hash table, we found our pair
        - If not, add current number and its index to hash table
        - Time: O(n), Space: O(n)

    >>> two_sum([3,4,5,6], 7)
    [0, 1]

    >>> two_sum([4,5,6], 10)
    [0, 2]

    >>> two_sum([5,5], 10)  
    [0, 1]

    >>> two_sum([-3,-4,5,6], 2)
    [0, 2]

    >>> two_sum([3,4,5,6,7,8,9,10], 27)  
    []

    """
    seen = {}  # hash table to store {number: index}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # If complement exists in hash table, we found our pair
        if complement in seen:
            return [seen[complement], i]
        
        # Add current number and its index to hash table
        seen[num] = i
    
    # No solution found
    return []

# Time complexity: O(n) - traversing the array once
# Space complexity: O(n) - storing the numbers in the hash table

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n** ALL TESTS PASSED. AWESOME WORK! **\n")