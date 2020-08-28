# invert_naray
Given an N-ary group, take the values an invert them. Since the group (graph, tree, etc) can be arbitrary, like the example below, it can be effectively represented in a flat list like a binary tree example

```
        0
      / | \
     /  |  \
    1   2   3
   /|\       \
  / | \      /\
 6  7  8    9 10
              /\
             11 12
```

The aforementioned graph is expressed in nested tuples. Any index that has it's own children will be wrapped
in its own tuple where the first index is the node and the second is reserved for the children

Here is an example graph represented in tuples
`(0, ((1, (6, 7, 8)), 2, (3, (9, (10, (11, 12))))))`