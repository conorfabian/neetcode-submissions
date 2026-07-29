class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        seen = set()
        def dfs(node):
            if node in seen:
                return

            seen.add(node)
            for nei in graph[node]:
                dfs(nei)

            return

        res = 0
        for i in range(n):
            if i not in seen:
                res += 1
                dfs(i)

        return res