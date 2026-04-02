class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def find_indegree(graph):
            in_degree = {node:0 for node in graph}
            for node in graph:
                for nei in graph[node]:
                    in_degree[nei] += 1
            return in_degree
        
        def topo_sort(graph):
            res = []
            q = deque()
            in_degree = find_indegree(graph)
            for node in in_degree:
                if in_degree[node] == 0:
                    q.append(node)
            
            while q:
                node = q.popleft()
                res.append(node)
                for nei in graph[node]:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 0:
                        q.append(nei)
            
            return len(res) == len(graph)
        
        graph = {node:[] for node in range(numCourses)}
        for b, a in prerequisites:
            graph[a].append(b)
        
        return topo_sort(graph)