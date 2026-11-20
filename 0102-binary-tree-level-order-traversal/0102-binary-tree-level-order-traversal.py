class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        q = [root]
        res = []

        while q:
            level = []

            for node in q:
                level.append(node.val)

            res.append(level)

            new_q = []
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)

            q = new_q

        return res