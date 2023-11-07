"""
House Robber 2 :
Given an integer array nums representing the amount of money 
of each house, return the maximum amount of money you can 
rob tonight without alerting the police, given that all houses are 
arranged in a circle. Robbing adjacent houses will alert the 
police via some security system. 
"""

def robbing2(houses: list[int]) -> int :
  if len(houses) in [0, 2]:
    return 0
  case1 = houses[0] + robbing2(houses[2:-1])
  case2 = robbing2(houses[1:])
  return max(case1, case2)

# tests :
def test_dummy():
  assert True

def test_robbing2_no_houses():
  max_amount=robbing2([])
  assert max_amount==0

def test_robbing2_1_house():
  max_amount=robbing2([10])
  assert max_amount==10

def test_robbing2_2_houses():
  max_amount=robbing2([10, 20])
  assert max_amount==0

def test_robbing2_3_houses_same_amount():
  max_amount=robbing2([10, 10, 10])
  assert max_amount==10

def test_robbing2_4_houses_diff_amount():
  max_amount=robbing2([1, 2, 3, 1])
  assert max_amount==4