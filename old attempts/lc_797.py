class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #edges cases:
        if not graph:
            return []
        
        # build di-graph - dictionary
        d = {}
        for i in range(len(graph)):
            d[i] = graph[i] # one-way link
        print(d)
        # apply DFS on DAG
        n = len(graph)
        stack = [(0, [0])] # - store both the (node, and the path leading to it)
        res = []
        while stack:
            node, path = stack.pop()
            # check leaf
            if node == n - 1:
                res.append(path)
            # traverse rest
            for nex in d[node]:
                stack.append((nex, path+[nex]))
        return res
