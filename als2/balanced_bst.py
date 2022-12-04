class BSTNode:
	
    def __init__(self, key, parent):
        self.NodeKey = key # ключ узла
        self.Parent = parent # родитель или None для корня
        self.LeftChild = None # левый потомок
        self.RightChild = None # правый потомок
        self.Level = 0 # уровень узла
        
class BalancedBST:
		
    def __init__(self):
        self.Root = None # корень дерева
  
    def GenerateTree(self, a):
	# создаём дерево с нуля из неотсортированного массива a

        a = sorted(a)
        self.generate(a, None, 0)
        return self.Root

    def generate(self, a, parent, level):
        if not a:
            return None
        if len(a) == 1:
            self.Root = BSTNode(a[0], parent)
            self.Root.Level = level
            return self.Root
        middle_index = len(a)//2
        root_key = a[middle_index]
        self.Root = BSTNode(root_key, parent)
        self.Root.Level = level
        self.Root.LeftChild = BalancedBST().generate(a[:middle_index], self.Root, level+1)
        self.Root.RightChild = BalancedBST().generate(a[middle_index:], self.Root, level+1)
        return self.Root

    def IsBalanced(self, root_node):
        return False