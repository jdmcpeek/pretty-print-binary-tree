Pretty-prints a binary tree with child fields `left` and `right`. Each node contains a `data` field, which is printed.

Run `python tree.py` and check out the results.

The tree may be of any depth, but usually after 6 levels it's too wide for most screens.

Looks best when the nodes' printed values are under 3 characters long (especially on leaf nodes).

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
