class BST:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    def insert(self,val):
        if val > self.val:
            if type(self.right) is BST:
                self.right.insert(val)
            else:
                self.right = BST(val)
        elif val < self.val:
            if type(self.left) is BST:
                self.left.insert(val)
            else:
                self.left = BST(val)
    def is_leaf(self):
        return (self.left is None and self.right is None)
    def find(self,val):
        if val == self.val:
            return self
        elif val > self.val:
            if not self.right.is_leaf():
                return self.right.find(val)
            elif self.right.val is val:
                return self.right
            else:
                return False
        elif val < self.val:
            if not self.right.is_leaf():
               return self.left.find(val)
            elif self.left.val is val:
                return self.left
            else:
                return False
    def __str__(self):
        return ('[{},{},{}]'.format(self.val,self.left,self.right))

            
    
                
me = BST(10)
me.insert(5)
me.insert(3)
me.insert(4)
me.insert(2)
me.insert(20)
me.insert(15)
me.insert(25)
print(me)
