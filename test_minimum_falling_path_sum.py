"""
Minimum Falling Path Sum :
Given an n x n array of integers matrix, return the minimum sum
of any falling path through matrix.

A falling path starts at any element in the first row and chooses
the element in the next row that is either directly below or
diagonally left/right. Specifically, the next element from
position (row, col) will be (row + 1, col - 1), (row + 1, col), or
(row + 1, col + 1).
"""
def min_falling_path(matrix: list[list[int]]) -> int:
    return min_falling_path_helper(matrix, set())

def min_falling_path_helper(matrix: list[list[int]], to_be_excluded: set[int]) -> int:
    N = len(matrix)
    if N==0:
        return 0
    
    if N>=1:
        cases = []
        """
        [2,1,3]
        [6,5,4]
        [7,8,9]
        """
        for i in range(0, N):
            if i not in to_be_excluded:
                cases += [matrix[0][i] + min_falling_path_helper(matrix[1:], set(range(i+2, N)))]
        return min(cases)

#Tests
def test_dummy():
    assert True

def test_min_falling_path_empty_matrix():
    assert min_falling_path([])==0

def test_min_falling_path_1x1_matrix_A():
    assert min_falling_path([[1]])==1

def test_min_falling_path_1x1_matrix_B():
    assert min_falling_path([[2]])==2
    
def test_min_falling_path_2x2_matrix():
    """
    10 + 11 = 21
    10 + 21 = 31
    20 + 11 = 31
    20 + 21 = 41
    """
    assert min_falling_path([[10, 20],
                             [11, 21]])==21


def test_min_falling_path():
    assert min_falling_path([[2,1,3],
                             [6,5,4],
                             [7,8,9]])==13