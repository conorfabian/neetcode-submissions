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
            for pre in graph[node]:
                if not dfs(pre): return False
            seen.remove(node)

            return True

        for i in range(numCourses):
            if not dfs(i): return False

        return True