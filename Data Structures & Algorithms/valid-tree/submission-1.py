class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        seen = set()
        def dfs(node, prev):
            if node in seen:
                return False

            seen.add(node)
            for nei in graph[node]:
                if nei == prev:
                    continue
                elif not dfs(nei, node): return False

            return True

        return dfs(0, -1) and len(seen) == n