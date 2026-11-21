
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        n = len(parent)

        # Step 1: Build original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Step 2: Store new parents
        new_parent = parent[:]

        # Store nearest ancestor for each character
        last = [-1] * 26

        def find_parents(node):

            char = ord(s[node]) - ord('a')

            # Save previous ancestor of this character
            previous = last[char]

            # Find matching ancestor
            if previous != -1:
                new_parent[node] = previous

            # Current node becomes nearest for this character
            last[char] = node

            # Visit original children
            for child in children[node]:
                find_parents(child)

            # Restore previous value
            last[char] = previous

        find_parents(0)

        # Step 3: Build modified tree
        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Step 4: Calculate subtree sizes
        answer = [0] * n

        def dfs(node):
            answer[node] = 1

            for child in new_children[node]:
                dfs(child)
                answer[node] += answer[child]

        dfs(0)

        return answer
