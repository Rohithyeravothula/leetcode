class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        mapper = {}
        newnode = Node(node.val, [])
        mapper[node] = newnode
        cur = [node]
        seen = set()
        while cur:
            nxt = []
            for val in cur:
                if val not in seen:
                    val = mapper[val]
                    for child in val.neighbors:
                        if child in mapper:
                            curval.neighbors.append(mapper[child])
                        else:
                            childnode = Node(child.val, [])
                            curval.neighbors.append(childnode)
                            mapper[child] = childnode

                        nxt.append(child)
                    seen.add(val)
            cur = nxt
        return newnode
"""
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4},{"$ref":"2"},{"$ref":"4"}],"val":3}],"val":2},{"$ref":"4"}],"val":1}
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}
"""
