def product_except_self(nums: list[int]) -> list[int]:
    """
    Given an array of integers, return an array where each element is the product of all other elements in the input array except itself.
    So for example,
    Input: [1, 2, 4, 6]

    For i = 0 (nums[0] = 1):
    Product of all except 1 → 2 * 4 * 6 = 48

    For i =1 (nums[1] = 2):
    Product of all except 2 → 1 * 4 * 6 = 24

    For i = 2 (nums[2] = 4):
    Product of all except 4 → 1 * 2 * 6 = 12

    For i = 3 (nums[3] = 6):
    Product of all except 6 → 1 * 2 * 4 = 8

    Edge Cases: 
    - Can the values be duplicated?
    - The values can be negative, zero, or positive.
    - Can the array be empty?
    - Will the resulting array always be the same length as the input array?

    Approach:
    1. Iterate throught the list and pop of the values at the current index.
    2. Calculate the product of the remaining numbers and store it in an array.
    3. Return the resulting array.
    >>> product_except_self([1, 2, 4, 6])
    [48, 24, 12, 8]
    >>> product_except_self([-1, 0, 1, 2, 3])
    [0, -6, 0, 0, 0]
    """
    output = [None] * len(nums)
    i = 0
    while i < len(nums):
        s = nums[:i] + nums[i+1:]
        product = 1
        for j in range(len(s)):
            product = product * s[j]
        output[i] = product
        i += 1
    return output

# Time Complexity: O(n^2) - We iterate through the list and for each element, we calculate the product of the remaining elements.
# Space Complexity: O(n) - We create a new list to store the output.

def product_except_self_optimized(nums: list[int]) -> list[int]:
    """
    Optimized version of product_except_self that calculates the product in O(n) time.
    This avoids the nested loop and uses two passes to calculate the left and right products.
    >>> product_except_self_optimized([1, 2, 4, 6])
    [48, 24, 12, 8]
    >>> product_except_self_optimized([-1, 0, 1, 2, 3])
    [0, -6, 0, 0, 0]
    """
    n = len(nums)
    output = [1] * n

    left_product = 1
    for i in range(n):
        output[i] = left_product
        left_product *= nums[i]

    right_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]

    return output

# Time Complexity: O(n) - We make two passes through the list.
# Space Complexity: O(n) - We create a new list to store the output.

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("All tests passed.")