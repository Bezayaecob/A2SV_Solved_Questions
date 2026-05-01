class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph= [[] for _ in range(n)]
        indegree= [0]*n
        queue= deque()
        for ancestor, child in edges:
            graph[ancestor].append(child)
            indegree[child]+=1
        
        ancestor=[set() for _ in range(n)]
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
            
        
        while queue:
            node = queue.popleft()
            for child in graph[node]:
                indegree[child]-=1


                ancestor[child].add(node)
                for x in (ancestor[node]):
                    ancestor[child].add(x)
                
                if indegree[child]==0:
                    queue.append(child)
                

        for i in range(n):
            ancestor[i] = sorted(ancestor[i])
        return ancestor