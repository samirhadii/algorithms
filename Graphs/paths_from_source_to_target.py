# leetcode 797
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
# find all possible paths from node 0 to node n - 1 and return them in any order.
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i
# (i.e., there is a directed edge from node i to node graph[i][j]).

# dfs approach to finding all paths in a DAG


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        start = 0
        target = len(graph) - 1
        output = []

        def dfs(node, path):
            if node == target:
                output.append(path.copy())
                return
            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()

        dfs(start, [0])
        return output
