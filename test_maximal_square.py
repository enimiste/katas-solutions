"""
Maximal Square :
Given an m x n binary matrix filled with 0's and 1's, find the
largest square containing only 1's and return its area.
"""
def max_square_area(matrix: list[list[int]]) -> int :
  M = len(matrix)
  if M==0:
    return 0
  if M==1:
    if len(matrix[0])==1:
      return 1 if matrix[0][0]==1 else 0
    
  if M>=2:
    N = len(matrix[0])
    if N>=1:
      max_area = 0
      for i in range(0, M):
        for j in range(0, N):
          if matrix[i][j]==1:
            k=0
            while (k+j)<N and (k+i)<M and matrix[i][k+j]==1 and matrix[k+i][k+j]==1:
              k += 1
            max_area = max(k*k, max_area)
      return max_area
  return 0

def test_dummy():
  assert True

def test_max_square_area_empty():
  assert max_square_area([])==0

def test_max_square_area_1x1_0_matrix():
  assert max_square_area([[0]])==0

def test_max_square_area_1x1_1_matrix():
  assert max_square_area([[1]])==1

def test_max_square_area_2x2_all_0_matrix():
  assert max_square_area([[0, 0], 
                          [0, 0]])==0

def test_max_square_area_2x2_all_1_matrix():
  assert max_square_area([[1, 1], 
                          [1, 1]])==4
  
def test_max_square_area_2x2_one_1_matrix():
  assert max_square_area([[1, 0], 
                          [0, 0]])==1
  assert max_square_area([[0, 1], 
                          [0, 0]])==1
  assert max_square_area([[0, 0], 
                          [0, 1]])==1
  
def test_max_square_area_2x2_two_1_matrix():
  assert max_square_area([[1, 1], 
                          [0, 0]])==1
  assert max_square_area([[0, 1], 
                          [0, 1]])==1
  assert max_square_area([[0, 0], 
                          [1, 1]])==1

def test_max_square_area_2x3_all_1_matrix():
  assert max_square_area([[1, 1, 1], 
                          [1, 1, 1]])==4
  
def test_max_square_area_2x3_creuse_1_matrix():
  assert max_square_area([[1, 0, 1], 
                          [1, 0, 1]])==1
  assert max_square_area([[1, 1, 0], 
                          [1, 1, 0]])==1
  
def test_max_square_area_2x3_creuse_1_matrix():
  assert max_square_area([[0, 1, 1], 
                          [0, 1, 1]])==4

def test_max_square_area():
  assert max_square_area([[1,0,1,0,0],
                          [1,0,1,1,1],
                          [1,1,1,1,1],
                          [1,0,0,1,0]])==4