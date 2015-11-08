class BST :

  root = None
  countNode = 0
  typeTree = None

  def __init__(self, root='empty', parent=None) :
    self.item   = root
    self.left   = None
    self.right  = None
    self.parent = parent
    if self.item != 'empty' :
      BST.countNode += 1
    if BST.countNode == 1 :
      BST.root     = self
      BST.typeTree = type(self.item)

  def insert(self, newElem) :
    if type(newElem) == BST.typeTree :
      current = BST.root
      while True :
        if newElem < current.item :
          if current.left == None :
            current.left = BST(newElem, current)
            return current.left
            break
          else :
            current = current.left
        else :
          if current.right == None :
            current.right = BST(newElem, current)
            return current.right
            break
          else :
            current = current.right
    else : print('error')

  @property
  def maximum(self) :
    current = BST.root
    while current.right != None :
      current = current.right
    print(repr(current.item), '- maximum')
  @property
  def minimum(self):
    current = BST.root
    while current.left != None :
      current = current.left
    print(repr(current.item), '- minimum')
  @property
  def _summa(self):
    if self.left == None and self.right == None :
      return self.item
    elif self.left != None and self.right == None :
      return self.item+self.left._summa
    elif self.right != None and self.left == None :
      return self.item+self.right._summa
    else :
      return self.item+self.left._summa+self.right._summa

  def search(self, key) :
    h = 0
    current = BST.root
    while True :
      if key < current.item :
        if current.left != None :
          current = current.left
          h += 1
        else : return None
      elif key > current.item :
        if current.right != None :
          current = current.right
          h += 1
        else : return None
      elif key == current.item :
        return current.item, h, current

  @staticmethod
  def inorder(tree) :
    if tree :
      BST.inorder(tree.left)
      print(repr(tree.item), end=' ')
      BST.inorder(tree.right)
  @staticmethod
  def preorder(tree) :
    if tree :
      print(repr(tree.item), end=' ')
      BST.preorder(tree.left)
      BST.preorder(tree.right)
  @staticmethod
  def postorder(tree) :
    if tree :
      BST.postorder(tree.left)
      BST.postorder(tree.right)
      print(repr(tree.item), end=' ')