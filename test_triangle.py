"""
Triangle:
Given a triangle array, return the minimum path sum from top
to bottom.

For each step, you may move to an adjacent number of the row
below. More formally, if you are on index i on the current row,
you may move to either index i or index i + 1 on the next row.
"""
def min_path_sum(triangle: list[list[int]]) -> int:
  if len(triangle)==0:
    return 0
  case1 = triangle[0][0] + min_path_sum(triangle[1:])
  case2 = triangle[0][0] + min_path_sum([row[1:] for row in triangle[1:]])
  return min(case1, case2)

def test_dummy():
  assert True

def test_min_path_sum_triangle_empty():
  assert min_path_sum([])==0

def test_min_path_sum_triangle_1_row():
  assert min_path_sum([[2]])==2

def test_min_path_sum_triangle_1_row_diff_val():
  assert min_path_sum([[3]])==3

def test_min_path_sum_triangle_2_rows():
  assert min_path_sum([[2],
                       [3,4]])==5
  
def test_min_path_sum_triangle_3_rows():
  assert min_path_sum([[2],
                       [3,4],
                       [6,5,7]])==10

def test_min_path_sum_triangle():
  """
  2
  3 4
  6 5 7
  4 1 8 3
  """
  assert min_path_sum([[2],
                       [3,4],
                       [6,5,7],
                       [4,1,8,3]])==11