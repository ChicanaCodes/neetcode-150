def has_duplicate(nums):
    """
    Given a list of numbers, check to see if any of the values appear
    more than once in the given list.

    Can have negative ints?
    Are the nums sorted? 

    Input: List of integers

    Output: Boolean True if duplicates, else False
    
    Pseudocode: 
    1. Create a lookup table to store the values and their counts
    2. Iterate through the list, and check if the value exists in the lookup table
    3. If it does not exist, add it and set it's count to 0
    4. If it does exist, add it and set it's count to count + 1
    5. Once we've iterated through the array, we want to iterate through the 
    lookup dictionary and return true if all the values in the dictionary are 1 
    """
    int_counts = {}
    for num in nums: 
        if num in int_counts:
            int_counts[num] = int_counts[num] + 1
        else: 
            int_counts[num] = 1
    
    # Check if any number appears more than once
    for count in int_counts.values():
        if count > 1:
            return True
    return False

def has_duplicate_optimized(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True  # Early return - we found a duplicate!
        seen.add(num)
    return False

def has_duplicate_set(nums):
    return len(nums) != len(set(nums))

def has_duplicate_counting_optimized(nums):
    int_counts = {}
    for num in nums:
        if num in int_counts:
            return True  # Early return when we find a duplicate
        int_counts[num] = 1
    return False

print(has_duplicate([1, 2, 3, 4]))  # Should print False
print(has_duplicate([1, 2, 3, 3]))  # Should print True

print(has_duplicate_optimized([1, 2, 3, 4]))  # Should print False
print(has_duplicate_optimized([1, 2, 3, 3]))  # Should print True

print(has_duplicate_set([1, 2, 3, 4]))  # Should print False
print(has_duplicate_set([1, 2, 3, 3]))  # Should print True