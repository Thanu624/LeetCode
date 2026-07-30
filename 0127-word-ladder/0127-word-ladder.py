class Solution:
    ALPH = 'abcdefghijklmnopqrstuvwxyz'

    def ladderLength(self, bw: str, ew: str, wl: List[str]) -> int:
        if ew not in wl:
            return 0

        wl = set(wl)
        q = deque([(bw, 1)])   # (word, depth), start at 1

        while q:        #   O(N) number of loops
            w, depth = q.popleft()

            # generate all of w's possible next sequences
            for pos in range(len(w)):       # O(L)
                for letter in self.ALPH:        # O(26)
                    # skip if it's the same letter
                    if letter == w[pos]:
                        continue

                    possible_next_w = w[:pos] + letter + w[pos+1:]      # O(L)
                    if possible_next_w == ew:
                        return depth+1

                    if possible_next_w in wl:
                        wl.remove(possible_next_w)      # remove from choices to ensure enqueue each str once
                        q.append((possible_next_w, depth+1))

        return 0