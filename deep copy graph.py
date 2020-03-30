class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def helper(node):
            if not node:
                return
            if node.val in graph:
                return graph[node.val]
            graph[node.val] = Node(node.val)
            for neighbor in node.neighbors:
                graph[node.val].neighbors.append(helper(neighbor))
            return graph[node.val]

        graph = {}
        return helper(node)


solution = Solution()
solution.cloneGraph([[2,4],[1,3],[2,4],[1,3]])