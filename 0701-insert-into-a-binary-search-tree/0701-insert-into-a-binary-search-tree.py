
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        return self.insert(root, val)

    def insert(self, root, val):
        if root is None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insert(root.left, val)

        elif val > root.val:
            root.right = self.insert(root.right, val)

        return root
