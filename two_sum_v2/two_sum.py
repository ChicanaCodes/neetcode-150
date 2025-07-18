def two_sum(numbers: list[int], target: int) -> list[int]:
    '''
    Problem;
    You're given an array of integers in sorted ascending order, 
    ex: [1, 2, 3, 4], and a target sum. Return the indices of the 
    2 numbers that add up to the target value.  

    Edge Cases: 
    - Can there be duplicates? No
    - Will there always be a solution? Yes
    - Can there be negatives? Yes
    - Is there a size restraint? Yes
    - Can the list be empty? No
    - Can use additional data structures? No O(1)    
    
    Approach: 
    1. Use two pointers, one at the start and one at the end of the list.
    2. Calculate the sum of the two pointers.
    3. If the sum is equal to the target, return the indices.
    4. If the sum is less than the target, move the left pointer to the right.
    5. If the sum is greater than the target, move the right pointer to the left.
    6. Repeat until the pointers meet.
    7. If no solution is found, return an empty list.
    >>> two_sum([1,2,3,4], 3)
    [1, 2]
    >>> two_sum([2,7,11,15], 9)
    [1, 2]
    >>> two_sum([2,3,4], 6)
    [1, 3]
    >>> two_sum([-1,0], -1)
    [1, 2]
    >>> two_sum([-3,3,4,90], 0)
    [1, 2]
    '''
    left, right = 0, len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []


# Time Complexity: O(n) - We traverse the list once with two pointers.
# Space Complexity: O(1) - We use constant space for the pointers and variables.
if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("All tests passed!")  