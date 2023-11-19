"""
Equal Sum Partition :
Given an integer array nums, return true if you can partition the 
array into two subsets such that the sum of the elements in 
both subsets is equal or false otherwise.
"""
def try_partition(nums: list[int]) -> bool:
  n = len(nums)
  if n<=1:
    return False
  nums_sum = sum(nums)
  if not nums_sum%2==0:
    return False

  return try_partition_helper(nums[1:], nums_sum//2-nums[0])

def try_partition_helper(nums: list[int], subset_sum_target: int) -> bool:
  if subset_sum_target<0:
    return False
  if subset_sum_target==0:
    return True
  return try_partition_helper(nums[1:], subset_sum_target-nums[0])

# tests :
def test_dummy():
  assert True

def test_equal_sum_empty_array():
  can_be_partitionned=try_partition([])
  assert not can_be_partitionned

def test_equal_sum_1_elem_array():
  can_be_partitionned=try_partition([1])
  assert not can_be_partitionned

def test_equal_sum_2_equal_elem_array():
  can_be_partitionned=try_partition([1, 1])
  assert can_be_partitionned

def test_equal_sum_3_equal_elem_array():
  can_be_partitionned=try_partition([1, 1, 1])
  assert not can_be_partitionned

def test_equal_sum_4_equal_elem_array():
  can_be_partitionned=try_partition([1, 1, 1, 1])
  assert can_be_partitionned

def test_equal_sum_3_diff_elem_array():
  can_be_partitionned=try_partition([2, 1, 1])
  assert can_be_partitionned

def hid_test_equal_sum():
  can_be_partitionned=try_partition([1,5,11,5])
  assert can_be_partitionned

def test_no_equal_sum():
  can_be_partitionned=try_partition([1,2,3,5])
  assert not can_be_partitionned