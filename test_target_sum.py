"""
Target Sum :
You are given an integer array nums and an integer target. You 
want to build an expression out of nums by adding one of the 
symbols '+' and '-' before each integer in nums and then 
concatenate all the integers.
Return the number of different expressions that you can build, 
which evaluates to target.
"""
def target_sum_combinations(nums: list[int], target: int) -> int:
  if len(nums)==0:
    return 0
  if len(nums)==1:
    return 1 if abs(nums[0])==abs(target) else 0

  case1 = target_sum_combinations(nums[1:], target-nums[0]) 
  case2 = target_sum_combinations(nums[1:], target+nums[0])   
  return case1 + case2

# tests :
def test_dummy():
  assert True

def test_target_sum_empty_array():
  nbr = target_sum_combinations([], 10)
  assert nbr==0

def test_target_sum_1_elem_equal_target():
  nbr = target_sum_combinations([1], 1)
  assert nbr==1

def test_target_sum_1_elem_equal_target_n1():
  nbr = target_sum_combinations([1], -1)
  assert nbr==1

def test_target_sum_1_elem_diff_target():
  nbr = target_sum_combinations([1], 2)
  assert nbr==0

def test_target_sum_2_elem_sum_up_to_target_0():
  nbr = target_sum_combinations([1, 1], 0)
  assert nbr==2

def test_target_sum_2_elem_sum_up_to_target():
  nbr = target_sum_combinations([1, 1], 2)
  assert nbr==1

def test_target_sum_2_elem_not_sum_up_to_target():
  nbr = target_sum_combinations([1, 1], 3)
  assert nbr==0

def test_target_sum_3_elem_sum_up_to_target():
  nbr = target_sum_combinations([1, 1, 1], 3)
  assert nbr==1

def test_target_sum():
  nbr = target_sum_combinations([1,1,1,1,1], 3)
  assert nbr==5
