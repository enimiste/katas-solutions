"""
Combination Sum 4 :
Given an array of distinct integers nums and a target integer 
target, return the number of possible combinations that add up 
to target.
Note that different sequences are counted as different 
combinations.
"""
def combinations(nums: list[int], target: int) -> int:
  return len(combinations_helper(nums, target, []))

def combinations_helper(nums: list[int], target: int, so_far: list[list[int]]) -> list[list[int]]:
  if target==0:
    return so_far
  if target<0:
    return []
  if len(nums)>=1:
    combs = []
    for i in range(0, len(nums)):
      # nums[i]
      if len(so_far)==0:
        new_so_far1 = [[nums[i]]]
      else:
        new_so_far1 = [sf + [nums[i]] for sf in so_far]
      combs += combinations_helper(nums, target - nums[i], new_so_far1) 
    return combs
  return []

# tests
def test_dummy():
  assert True

def test_combinations_1_elem_zero():
  assert combinations([1], 0)==0

def test_combinations_1_elem_equal_target():
  assert combinations([1], 1)==1

def test_combinations_1_elem_gt_target():
  assert combinations([2], 1)==0

def test_combinations_1_elem_lt_target():
  assert combinations([1], 2)==1

def test_combinations_2_elem_without_1():
  """
  (2,3)
  (3,2)
  """
  assert combinations([2, 3], 5)==2

def test_combinations_2_elem():
  """
  (1,1,1)
  (1,2)
  (2,1)
  """
  assert combinations([1, 2], 3)==3

def test_combinations_2_elem_ko():
  assert combinations([2, 4], 5)==0

def test_combinations_2_elem_ko():
  assert combinations([2, 4], 5)==0

def test_combinations_3_elem_lt_target():
  """
  (1,1,1,1)
  (1,1,2)
  (1,3)
  (1,2,1)
  (3,1)
  (2,1,1)
  (2,2)
  """
  assert combinations([1,2,3], 4)==7



