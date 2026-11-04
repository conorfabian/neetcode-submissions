class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for course, pre in prerequisites:
            graph[course].append(pre)

        seen = set()
        def dfs(node):
            if node in seen:
                return False

            seen.add(node)
            for child in graph[node]:
                if not dfs(child):
                    return False
            seen.remove(node)
            graph[node] = []
            return True

        for n in range(numCourses):
            if not dfs(n):
                return False

        return True