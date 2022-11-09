class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key  # ключ узла
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок

    def have_children(self):
        return self.LeftChild and self.RightChild


class BSTFind:  # промежуточный результат поиска
    def __init__(self):
        self.Node = None  # None если
        # в дереве вообще нету узлов

        self.NodeHasKey = False  # True если узел найден
        self.ToLeft = False  # True, если родительскому узлу надо
        # добавить новый узел левым потомком


class BST:
    def __init__(self, node):
        self.Root = node  # корень дерева, или None

    def FindNodeByKey(self, key):
        result = BSTFind()
        node = self.Root
        while node is not None:
            if node.NodeKey == key:
                result.Node = node
                result.NodeHasKey = True
                return result
            if node.NodeKey > key and node.LeftChild:
                result.ToLeft = True
                node = node.LeftChild
            if node.NodeKey > key and not node.LeftChild:
                result.ToLeft = True
                result.Node = node
                return result
            if node.NodeKey < key and node.RightChild:
                result.ToLeft = False
                node = node.RightChild
            if node.NodeKey < key and not node.RightChild:
                result.Node = node
                return result
        return result

    def AddKeyValue(self, key, val):
        find_result = self.FindNodeByKey(key)
        if find_result.NodeHasKey:
            return False  # если ключ уже есть
        parent_node = find_result.Node
        new_node = BSTNode(key, val, parent_node)
        if not parent_node:
            self.Root = new_node
            return
        if find_result.ToLeft:
            parent_node.LeftChild = new_node
        else:
            parent_node.RightChild = new_node

    def FinMinMax(self, FromNode, FindMax):
        node = FromNode if FromNode else self.Root
        if not node:
            return None
        child = node.RightChild if FindMax else node.LeftChild
        if not child:
            return node
        return self.FinMinMax(child, FindMax)

    def DeleteNodeByKey(self, key):
        find_result = self.FindNodeByKey(key)
        if not find_result.NodeHasKey:
            return False
        node_to_delete = find_result.Node
        if (
            not node_to_delete.have_children()
            and node_to_delete.Parent.LeftChild == node_to_delete
        ):
            node_to_delete.Parent.LeftChild = None
            node_to_delete.Parent = None
            return
        if (
            not node_to_delete.have_children()
            and node_to_delete.Parent.RightChild == node_to_delete
        ):
            node_to_delete.Parent.RightChild = None
            node_to_delete.Parent = None
            return
        if node_to_delete.LeftChild and not node_to_delete.RightChild:
            node_to_delete.LeftChild.Parent = node_to_delete.Parent
        return

    # узлом-преемником, ключ которого -- наименьший из всех ключей, которые больше ключа удаляемого узла.
    def Count(self):
        if self.Root is None:
            return 0
