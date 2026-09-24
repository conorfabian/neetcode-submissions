class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = { i: list() for i in range(numCourses)}

        for course, pre in prerequisites:
            graph[course].append(pre)

        seen = set()
        def dfs(node):
            if node in seen:
                return False

            seen.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            seen.remove(node)
            graph[node] = []

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True