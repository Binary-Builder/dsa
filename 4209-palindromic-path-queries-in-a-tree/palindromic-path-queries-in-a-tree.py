class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        i += 1
        while i <= self.n:
            self.tree[i] ^= val
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res ^= self.tree[i]
            i -= i & -i
        return res

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        s = list(s)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = n.bit_length()
        up = [[-1] * LOG for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix = [0] * n
        timer = 0

        # DFS to compute LCA binary lifting table, prefix masks, and Euler tour times
        def dfs(u, p, d, cur_mask):
            nonlocal timer
            depth[u] = d
            up[u][0] = p
            for i in range(1, LOG):
                if up[u][i - 1] != -1:
                    up[u][i] = up[up[u][i - 1]][i - 1]
            
            cur_mask ^= (1 << (ord(s[u]) - ord('a')))
            prefix[u] = cur_mask
            tin[u] = timer
            timer += 1

            for v in adj[u]:
                if v != p:
                    dfs(v, u, d + 1, cur_mask)
            tout[u] = timer - 1

        dfs(0, -1, 0, 0)

        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for i in range(LOG - 1, -1, -1):
                if depth[u] - (1 << i) >= depth[v]:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != -1 and up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]

        bit = FenwickTree(n)
        ans = []

        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]
                old_char = s[u]
                if old_char != new_char:
                    diff = (1 << (ord(old_char) - ord('a'))) ^ (1 << (ord(new_char) - ord('a')))
                    s[u] = new_char
                    bit.update(tin[u], diff)
                    bit.update(tout[u] + 1, diff)
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                
                mask_u = prefix[u] ^ bit.query(tin[u])
                mask_v = prefix[v] ^ bit.query(tin[v])
                mask_lca = 1 << (ord(s[lca]) - ord('a'))
                
                path_mask = mask_u ^ mask_v ^ mask_lca
                
                # Check if path_mask has at most one bit set
                is_palindrome = (path_mask == 0) or ((path_mask & (path_mask - 1)) == 0)
                ans.append(is_palindrome)

        return ans