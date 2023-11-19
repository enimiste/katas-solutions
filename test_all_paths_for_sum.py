"""
Find all paths for a sum :
Given a binary tree and a number 'S', find all paths from
root-to-leaf such that the sum of all the node values of each path equals 'S'.

Data structures :
Node : {value: int, "left": Node|None, "right": Node|None}

Returns : list[list[int]] assuming tree values are unique
"""
# solution
def find_paths_for(root: dict, target_sum: int) -> list[list[int]]:
    if len(root.keys())==0:
        return []
    return find_paths_for_helper(root, target_sum, [])

def find_paths_for_helper(root: dict, target_sum: int, paths: list[list[int]]) -> list[list[int]]:
    print([target_sum, paths])
    if target_sum<0:
        return []
    if target_sum==0 and root is None:
        return paths
    if len(paths)==0:
        new_paths=[[root["val"]]]
    else:
        new_paths=[p+[root["val"]] for p in paths]

    if root["left"] is None and root["right"] is None:
        if target_sum-root["val"]==0:
            return new_paths
    xs, ys = [], []
    if root["left"] is not None:
        xs = find_paths_for_helper(root["left"], target_sum-root["val"], new_paths)
    if root["right"] is not None:
        ys = find_paths_for_helper(root["right"], target_sum-root["val"], new_paths)
    return xs + ys
    
# Tests
def test_dummy():
    assert True

def test_empty_tree():
    assert find_paths_for({}, 22)==[]

def test_one_node_tree_val_22():
    tree = {
            "val": 22,
            "left": None,
            "right": None
        }
    assert find_paths_for(tree, 22)==[[22]]

def test_two_nodes_left_tree_sum_to_22():
    tree = {
            "val": 12,
            "left": {
                "val": 10,
                "left": None,
                "right": None
            },
            "right": None
        }
    assert find_paths_for(tree, 22)==[[12, 10]]

def test_two_nodes_right_tree_sum_to_22():
    tree = {
            "val": 20,
            "right": {
                "val": 2,
                "left": None,
                "right": None
            },
            "left": None
        }
    assert find_paths_for(tree, 22)==[[20, 2]]

def test_three_nodes_all_left_tree_sum_to_22():
    tree = {
            "val": 12,
            "left": {
                "val": 6,
                "left": {
                    "val": 4,
                    "left": None,
                    "right": None
                },
                "right": None
            },
            "right": None
        }
    assert find_paths_for(tree, 22)==[[12, 6, 4]]

def test_four_nodes_tree_sum_to_22():
    tree = {
            "val": 12,
            "left": {
                "val": 10,
                "left": None,
                "right": None
            },
            "right": {
                "val": 6,
                "left": {
                    "val": 4,
                    "left": None,
                    "right": None
                },
                "right": None
            }
        }
    assert find_paths_for(tree, 22)==[[12, 10], [12, 6, 4]]

def test_four_nodes_tree_sum_to_22_ko():
    tree = {
            "val": 12,
            "left": {
                "val": 10,
                "left": None,
                "right": None
            },
            "right": {
                "val": 6,
                "left": {
                    "val": 4,
                    "left": {
                        "val": 10,
                        "left": None,
                        "right": None
                    },
                    "right": None
                },
                "right": None
            }
        }
    assert find_paths_for(tree, 22)==[[12, 10]]


def test_all_paths_found():
    tree = {"val": 5, 
            "left": {
                "val": 4,
                "left": {
                    "val": 11,
                    "left": {
                        "val": 7,
                        "left": None,
                        "right": None
                    },
                    "right": {
                        "val": 2,
                        "left": None,
                        "right": None
                    }
                },
                "right": None
            },
            "right": {
                "val": 8,
                "left": {
                    "val": 13,
                    "left": None,
                    "right": None
                },
                "right": {
                    "val": 4,
                    "left": None,
                    "right": {
                        "val": 4,
                        "left": None,
                        "right": {
                            "val": 1,
                            "left": None,
                            "right": None
                        }
                    }
                }
            }
        }
    assert find_paths_for(tree, 22)==[
                                        [5, 4, 11, 2],
                                        [5, 8, 4, 4, 1],
                                        ]