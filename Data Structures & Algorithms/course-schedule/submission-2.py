class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)

        seen = set()
        def dfs(course):
            if course in seen:
                return False
            elif not graph[course]:
                return True

            seen.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            seen.remove(course)
            graph[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True