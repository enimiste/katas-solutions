"""
Delete and Earn :
You are given an integer array nums. You want to maximize the 
number of points you get by performing the following operation 
any number of times:

Pick any nums[i] and delete it to earn nums[i] points. 
Afterwards, you must delete every element equal to nums[i]-1 
and every element equal to nums[i]+1. 

Return the maximum number of points you can earn by 
applying the above operation some number of times.
"""

def delete_and_earn(nums: list[int]) -> int:
  if len(nums)==0:
    return 0

  if len(nums)==1:
    return nums[0]

  cases = []
  for i in range(0, len(nums)):
    cases += [nums[i] + delete_and_earn([x for x in nums if x not in {nums[i], nums[i]-1, nums[i]+1}])]
  return max(cases)
  
# tests
def test_dummy():
  assert True

def test_delete_earn_empty_array():
  assert delete_and_earn([])==0

def test_delete_earn_1_elem_array():
  assert delete_and_earn([2])==2


def test_delete_earn_2_elem_array_canceled_each_other():
  assert delete_and_earn([1, 2])==2

def test_delete_earn_2_elem_array():
  assert delete_and_earn([1, 7])==8

def test_delete_earn_3_array_caseA():
  assert delete_and_earn([3,4,2])==6

def test_delete_earn_3_array_caseB():
  assert delete_and_earn([2,5,4])==7

def test_delete_earn_3_array_with_dup():
  assert delete_and_earn([2,5,5])==7

def test_delete_earn_3_neg_elem_array():
  assert delete_and_earn([-2,-5,-4])==-6

def test_delete_earn_4_array_caseA():
  assert delete_and_earn([3,4,2,2])==6
