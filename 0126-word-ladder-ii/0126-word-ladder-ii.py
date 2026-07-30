class Node:
    def __init__(self, word: str):
        self.word = word
        self.edges = set()

    def add_edges(self, *nodes):
        self.edges.update(nodes)

    def __hash__(self):
        return hash(self.word)

    def __eq__(self, other: "Node"):
        return other.word == self.word

    def __repr__(self):
        return f"Node{{{self.word}}}"

def masks(word):
    i = 0
    while i < len(word):
        yield word[:i] + "*" + word[i+1:]
        i += 1

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        # Build the word graph
        wordmap = {}
        neighbours = [None] * len(beginWord)

        for word in wordList:
            if word in wordmap:
                continue
            i = 0
            wnode = Node(word)
            wordmap[word] = wnode
            for mask in masks(word):
                if mask not in wordmap:
                    node = Node(mask)
                    wordmap[mask] = node
                else:
                    node = wordmap[mask]

                node.add_edges(wnode)
                neighbours[i] = node
                i += 1
            
            wnode.add_edges(*neighbours)

        queue = deque()
        for mask in masks(beginWord):
            if mask in wordmap:
                queue.append((3, wordmap[mask]))

        # ==== BFS, propagating one step in each iteration ==== 
        found = False
        touched = set()
        levels = {}

        while queue and not found:
            for i in range(len(queue)):
                depth, node = queue.popleft()

                if node.word == endWord:
                    found = True
                    break

                if node in touched:
                    continue

                if depth not in levels:
                    levels[depth] = set()
                levels[depth].add(node)

                touched.add(node)

                for neighbour in node.edges:
                    if neighbour not in touched:
                        queue.append((depth + 1, neighbour))

        if not found:
            return []

        # ==== Go backwards from the endWords. Either BFS or DFS works here ====
        result = []
        st = [(depth, wordmap[endWord], [endWord])]

        while st:
            depth, node, path = st.pop()

            # We started our search from depth 3, so we can stop searching here
            if depth == 3:
                result.append([beginWord] + path)
                continue

            next_lvl =  levels[depth - 1]

            for neighbour in node.edges:
                if neighbour not in next_lvl:
                    continue

                # I know this is a little weird, keep in mind that only
                # the words at even steps are real words, while odd steps are masks
                # so if we are at an odd depth, neighbour must be a word
                if depth % 2 == 1:
                    new_path = [neighbour.word] + path
                else:
                    new_path = path

                st.append((depth - 1, neighbour, new_path))

        return result