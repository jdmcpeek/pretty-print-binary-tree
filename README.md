Run `python tree.py` and check out the results.

```python
# prep the tree...
# 
# layer 1
root = Node('A')

# layer 2
root.left = Node('B')
root.right = Node('C')

# layer 3
root.left.left = Node('D')
root.left.right = Node('E')

# add a sub-tree ('X' nodes) using the createTree method
root.left.right.right = Node.createTree(2)

root.right.left = Node('F')
root.right.right = Node('G')

# layer 3
root.left.left.left = Node('H')
root.left.left.right = Node('I')
root.left.right.left = Node('J')
root.right.right.left = Node('N')
root.right.right.right = Node('O')

root.prettyPrint()


```

                  --------------A-------------- 
                 /                             \
          ------B------                   ------C------ 
         /             \                 /             \
      --D--           --E--             F             --G-- 
     /     \         /     \                         /     \
    H       I       J       X                       N       O 
                           / \                                
                          X  XX                                
