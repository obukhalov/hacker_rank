#!/bin/python3

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def find_all_leaves(root):
    need_to_visit = [root]
    tree = []

    while len(need_to_visit) != 0:
        node = need_to_visit.pop()
        tree.append(node.info)
        if node.left:
            need_to_visit.append(node.left)
        if node.right:
            need_to_visit.append(node.right)

    return tree

def lca(root, v1, v2):
    #Enter your code here
    need_to_visit = [root]
    roots_dict = {}

    while len(need_to_visit) != 0:
        node = need_to_visit.pop()
        roots_dict[node] = find_all_leaves(node)
        if node.left:
            need_to_visit.append(node.left)
        if node.right:
            need_to_visit.append(node.right)

    _len = len(roots_dict)
    common_root = root
    for key in roots_dict:
        if v1 in roots_dict[key] and v2 in roots_dict[key] and len(roots_dict[key]) < _len:
            common_root = key

    return common_root

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
