class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []


class SimpleTree:
    def __init__(self, root):
        self.Root = root

    def AddChild(self, ParentNode, NewChild):
        parent_node = self.FindNodesByValue(ParentNode.NodeValue)[0]
        NewChild.Parent = parent_node
        parent_node.Children.append(NewChild)

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete.Parent:
            NodeToDelete.Parent.Children.remove(NodeToDelete)
            NodeToDelete.Parent = None

    def GetAllNodes(self):
        def find_nodes(node):
            result.append(node)
            for children_node in node.Children:
                find_nodes(children_node)

        result = []
        node = self.Root
        find_nodes(node)
        return result

    def FindNodesByValue(self, val):
        def find_nodes(node):
            if node.NodeValue == val:
                result.append(node)
            for children_node in node.Children:
                find_nodes(children_node)

        result = []
        node = self.Root
        find_nodes(node)
        return result

    def MoveNode(self, OriginalNode, NewParent):
        OriginalNode.Parent.Children.remove(OriginalNode)
        OriginalNode.Parent = NewParent
        NewParent.Children.append(OriginalNode)

    def Count(self):
        return len(self.GetAllNodes())

    def LeafCount(self):
        return len([node for node in self.GetAllNodes() if not node.Children])

    def EvenTrees(self):
        res = []
        if not self.Root.Children:
            return []
        for child in self.Root.Children:
            subtree = SimpleTree(child)
            if subtree.Count() % 2 == 0:
                res.append(subtree.Root.Parent)
                res.append(subtree.Root)
                res += subtree.EvenTrees()
            else:
                res += subtree.EvenTrees()
        return res
