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
            for edge in graph[node]:
                if edge == prev:
                    continue
                elif not dfs(edge, node):
                    return False

            return True

        return dfs(0, -1) and n == len(seen)