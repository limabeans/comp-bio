class Node:
    def __init__(self, v=None):
        self.val = v
        self.children = []

class Edge:
    def __init__(self,s):
        self.label = s
        self.child = None


def getPrefixEndIndex(s1, s2):
    ind = 0
    while ind < len(s1) and ind < len(s2) and s1[ind]==s2[ind]:
        ind+=1
    return ind


def insertSubstring(root, substr, suffixIndex):
    ind = 0
    for edge in root.children:
        label = edge.label
        ind = getPrefixEndIndex(substr, label)
        if ind > 0:
            if ind == len(label):
                insertSubstring(edge.child, substr[ind:], suffixIndex)
            elif ind < len(label):
                midEdge = Edge(label[:ind])
                midNode = Node()
                root.children.remove(edge)
                oldEdge = edge
                root.children.append(midEdge)
                midEdge.child = midNode
                oldEdge.label = label[ind:]
                midNode.children.append(oldEdge)
                insertSubstring(midNode, substr[ind:], suffixIndex)
            return
    ##
    if ind == 0:
        newEdge = Edge(substr)
        root.children.append(newEdge)
        newEdge.child = Node(suffixIndex)

        

def buildSuffixTree(S):
    root = Node()
    for i in range(len(S)):
        suffix = S[i:]
        insertSubstring(root, suffix, i+1)
    return root


tree = buildSuffixTree('asdf$')

def bfs(root):
    queue = [(root, 0)]
    edgeLabels = []
    nodeVals = []
    while queue:
        curr, depth = queue.pop(0)
        nodeVals.append((str(curr.val), depth+1))
        for edge in curr.children:
            edgeLabels.append((edge.label, depth))
            queue.append((edge.child, depth+1))
    return (edgeLabels,nodeVals)

edges,nodes = bfs(tree)

print 'edges',edges
print 'nodes',nodes

