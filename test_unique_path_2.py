"""
Unique Paths 2 :
You are given an m x n integer array grid. There is a robot
initially located at the top-left corner (i.e., grid[0][0]). The robot
tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in
time.

An obstacle and space are marked as 1 or 0 respectively in grid.
A path that the robot takes cannot include any square that is an
obstacle. Return the number of possible unique paths that the
robot can take to reach the bottom-right corner.
"""
def unique_paths(rows_count: int, cols_count: int, obstacles: set[(int, int)]) -> int:
  print([rows_count, cols_count])
  if rows_count==0 or cols_count==0:
    return 0
  if rows_count==1 and cols_count==1:
    return 1 if (rows_count-1, cols_count-1) not in obstacles else 0
  
  case1, case2=(0,0)
  if (rows_count, cols_count-1) not in obstacles:
    case1 = unique_paths(rows_count, cols_count-1, obstacles)

  if (rows_count-1, cols_count) not in obstacles:
    case2 = unique_paths(rows_count-1, cols_count, obstacles)
  
  return case1 + case2 

def test_dummy():
  assert True

def test_unique_path_on_empty_grid():
  assert unique_paths(0,0, [])==0

def test_unique_path_on_1x1_grid_no_obst():
  assert unique_paths(1,1, [])==1

def test_unique_path_on_1x1_grid():
  assert unique_paths(1,1, [(0,0)])==0

def test_unique_path_on_1x2_grid_no_obst():
  assert unique_paths(1,2, [])==1

def test_unique_path_on_1x2_grid_caseA():
  assert unique_paths(1,2, [(0,0)])==0

def hid_test_unique_path_on_1x2_grid_caseB():
  assert unique_paths(1,2, [(1,1)])==0

def test_unique_path_on_1x99_grid_no_obst():
  assert unique_paths(1,99, [])==1

def test_unique_path_on_99x1_grid_no_obst():
  assert unique_paths(99,1, [])==1

def test_unique_path_on_2x2_grid_no_obst():
  assert unique_paths(2,2, [])==2

def test_unique_path_on_3x3_grid_no_obst():
  assert unique_paths(3,3, [])==6

def test_unique_path_on_3x3_grid():
  assert unique_paths(3,3, [(0,0)])==0

def hid_test_unique_path_on_3x3_grid():
  assert unique_paths(3,3, [(1,1)])==2

def test_unique_paths_no_obst():
  assert unique_paths(3, 7, [])==28