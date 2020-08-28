import invert_naray


TREE1_A = (1,  ((2, (4, 5)), 
                (3, (6, 7))))
TREE1_B = (1,  ((3, (7, 6)),
                (2, (5, 4))))

TREE2_A = (1, (2, 
               (3, ((6, (12, 13)), 
                    (7, ((14, (19, 
                               20, 
                               (21, (25, 
                                     26,
                                     (27, (28, 29, 30)))))),
                         15)))), 
               (4, (8,)), 
               (5, (9,
                    (10, (16, 
                          (17, (22, 23, 24)),
                          18)),
                    11))))

TREE2_B = (1, ((5, (11, 
                    (10, (18, (17, (24, 23, 22)), 16)),
                    9)), 
               (4, (8,)), 
               (3, ((7, (15, 
                         (14, ((21, ((27, (30, 29, 28)),
                                     26, 
                                     25)), 
                               20,
                               19)))),
                    (6, (13, 12)))), 
               2))


def run_tests():
    assert invert_naray.invert(TREE1_A) == TREE1_B, "Tree 1 failed to invert correctly"
    assert invert_naray.invert(TREE2_A) == TREE2_B, "Tree 2 failed to invert correctly"


def _main():
    run_tests()


if __name__ == '__main__':
    _main()