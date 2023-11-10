"""
Unique Paths :
There is a robot on an m x n grid. The robot is initially located at
the top-left corner (i.e., grid[0][0]). The robot tries to move to
the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can
only move either down or right at any point in time.

Given the two integers m and n, return the number of possible
unique paths that the robot can take to reach the bottom-right
corner.
"""
def unique_paths(rows_count: int, cols_count: int) -> int:
  if rows_count==0 or cols_count==0:
    return 0
  if rows_count==1 or cols_count==1:
    return 1
  return unique_paths(rows_count, cols_count-1) + unique_paths(rows_count-1, cols_count)

def test_dummy():
  assert True

def test_unique_path_on_empty_grid():
  assert unique_paths(0,0)==0

def test_unique_path_on_1x1_grid():
  assert unique_paths(1,1)==1

def test_unique_path_on_1x2_grid():
  assert unique_paths(1,2)==1

def test_unique_path_on_1x99_grid():
  assert unique_paths(1,99)==1

def test_unique_path_on_99x1_grid():
  assert unique_paths(99,1)==1

def test_unique_path_on_2x2_grid():
  assert unique_paths(2,2)==2

def test_unique_paths():
  assert unique_paths(3, 7)==28