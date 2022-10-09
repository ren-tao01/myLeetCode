class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        nsize = len(graph)
        self.allPaths = list()

        count = 0
        for node in graph:
            
            for n in node:
                path = list()
                path.append(count)
                path.append(n)
                for g in graph.index(n):
                    temp = path.append(g)
                    g = temp

            count +=1




        return self.allPaths


        
            

        
            