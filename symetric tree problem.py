class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        def isMirror(t1, t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            return (t1.value == t2.value) and \
                   isMirror(t1.left, t2.right) and \
                   isMirror(t1.right, t2.left)
        
        return isMirror(root, root)

# Example usage: Creating a symmetric tree
if __name__ == "__main__":
    # Symmetric tree structure:
    #         1
    #       /   \
    #      2     2
    #     / \   / \
    #    3   4 4   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    # Create an instance of Solution
    solution = Solution()

    # Check if the tree is symmetric
    print(solution.isSymmetric(root))  # Output: True
