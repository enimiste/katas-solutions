"""
Minimum Path Sum :
Given a m x n grid filled with non-negative numbers, find a path
from top left to bottom right, which minimizes the sum of all
numbers along its path. You can only move either down or right
at any point in time.
"""
def min_path_sum(grid: list[list[int]]) -> int:
  if len(grid)==0:
    return 0
  return min_path_sum_helper(grid, 0)

def min_path_sum_helper(grid: list[list[int]], sum_so_far: int) -> int:
  if len(grid)==0:
    return None
  
  if len(grid)==1:
    if len(grid[0])==1:
      return grid[0][0] + sum_so_far
    
  if len(grid[0])==0:
    return None
  
  case1 = min_path_sum_helper([row[1:] for row in grid], sum_so_far+grid[0][0])
  case2 = min_path_sum_helper([row for row in grid[1:]], sum_so_far+grid[0][0])

  if case1 is not None and case2 is not None:
    return min(case1, case2)
  elif case1 is not None:
    return case1
  else:
    return case2

def test_dummy():
  assert True

def test_min_path_empty_grid():
  assert min_path_sum([])==0

def test_min_path_1x1_grid():
  assert min_path_sum([[1]])==1

def test_min_path_1x2_grid():
  assert min_path_sum([[1, 2]])==3

def test_min_path_2x2_grid():
  assert min_path_sum([ [1, 2], 
                        [3, 4]])==7 #1+2+4

def test_min_path_2x1_grid():
  assert min_path_sum([[1], 
                       [2]])==3

def test_min_path_sum():
  assert min_path_sum([[1,3,1],[1,5,1],[4,2,1]])==7