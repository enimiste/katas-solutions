"""
House Robber :
Given an integer array nums representing the amount of money 
of each house, return the maximum amount of money you can 
rob tonight without alerting the police. Robbing adjacent 
houses will alert the police via some security system.
"""
def robbing(houses: list[int]) -> int :
  if len(houses)==0:
    return 0
  case1 = houses[0] + robbing(houses[2:])
  case2 = robbing(houses[1:])
  return max(case1, case2)

# tests :
def test_dummy():
  assert True

def test_robbing_no_houses():
  max_amount=robbing([])
  assert max_amount==0

def test_robbing_1_house():
  max_amount=robbing([10])
  assert max_amount==10

def test_robbing_2_houses():
  max_amount=robbing([10, 20])
  assert max_amount==20

def test_robbing_3_houses_same_amount():
  max_amount=robbing([10, 10, 10])
  assert max_amount==20

def test_robbing_4_houses_same_amount():
  max_amount=robbing([10, 10, 10, 10])
  assert max_amount==20

def test_robbing_4_houses_diff_amount():
  max_amount=robbing([10, 20, 30, 40])
  assert max_amount==60

def test_robbing_5_houses_diff_amount():
  max_amount=robbing([2,7,9,3,1])
  assert max_amount==12