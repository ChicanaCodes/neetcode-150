class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    '''
    Given a tree, we want to swap the left and right children of every node.
    This can be done using a depth-first search (DFS) approach, where we recursively
    traverse the tree and swap the children of each node.
    
    Edge Cases:
    - Can the tree be empty? Yes, return None.
    - Can the tree have only one node? Yes, return the node itself.
    - Can the tree be unbalanced? Yes, the algorithm should handle it.
    - Can the tree have negative values? Yes, the algorithm should handle it.
    - Can the tree have duplicate values? Yes, the algorithm should handle it.
    - Is there a size restraint? No, the algorithm should handle large trees.
    >>> root = TreeNode(4)
    >>> root.left = TreeNode(2)
    >>> root.right = TreeNode(7)
    >>> root.left.left = TreeNode(1)
    >>> root.left.right = TreeNode(3)
    >>> root.right.left = TreeNode(6)
    >>> root.right.right = TreeNode(9)
    >>> inverted = invert_tree(root)
    >>> inverted.val
    4
    >>> inverted.left.val
    7
    >>> inverted.right.val
    2
    >>> inverted.left.left.val
    9
    >>> inverted.left.right.val
    6
    >>> inverted.right.left.val
    3
    >>> inverted.right.right.val
    1
    '''
    if root is None:
        return None
    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)
    return root


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("All tests passed!")

# Time Complexity: O(n) - We visit each node once.
# Space Complexity: O(h) - The space complexity is O(h) where h is the height of the tree due to the recursion stack.