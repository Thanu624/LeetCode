# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(arr):
            if len(arr)==0:
                return
            val=max(arr)
            index=arr.index(val)
            root=TreeNode(val)
            root.val=val
            root.left=dfs(arr[:index])
            root.right=dfs(arr[index+1:])
            return root
        return dfs(nums)