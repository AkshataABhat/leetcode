from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj_list=defaultdict(list)
        
        for node1,node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)
            
            
        queue=([source])
        visited=set([source])
        
        
        while queue:
            node=queue.pop(0)
            
            
            if node==destination:
                return True
            
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
                    
        return False

            
        
        