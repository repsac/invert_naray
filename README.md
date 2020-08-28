# invert_naray
Given an N-ary group, take the values and invert them left to right. Since the group (graph, tree, etc) can be arbitrary, like the example below, it can be effectively represented in a flat list like a binary tree example

```
            0
          / | \
         /  |  \
        1   2   3
       /|\       \
      / | \      /\
     6  7  8    9 10
                  /\
                 /  \
                11  12
```

The aforementioned graph is expressed in nested tuples.
Any index that has it's own children will be wrapped
in its own tuple where the first index is the node and
the second is reserved for the children

Here is an example graph represented in tuples
`(0, ((1, (6, 7, 8)), 2, (3, (9, (10, (11, 12))))))`

The resulting graph would then look like
```
            0
          / | \
         /  |  \
        3   2   1
       /\      /|\
      10 9    / | \
        /\   8  7  6
       /  \ 
      12  11
```