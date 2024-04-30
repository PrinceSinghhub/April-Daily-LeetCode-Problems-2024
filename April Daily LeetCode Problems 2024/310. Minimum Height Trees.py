class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<2:
            return [0]
        adj=[set() for _ in range(n)]
        for src,dst in edges:
            adj[src].add(dst)
            adj[dst].add(src)
        leaves=[node for node in range(n) if len(adj[node])==1]
        while n>2:
            n-=len(leaves)
            leavesNext=[]
            for leaf in leaves:
                neb=adj[leaf].pop()
                adj[neb].remove(leaf)
                if len(adj[neb])==1:
                    leavesNext.append(neb)
            leaves=leavesNext
        return leaves