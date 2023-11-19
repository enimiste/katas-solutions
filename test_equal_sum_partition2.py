"""
Equal Sum Partition 2 :
Given an integer array nums, return (list1, list2) if you can partition the 
array into two subsets such that the sum of the elements in 
both subsets is equal or None otherwise.
"""
def try_partition(nums: list[int]) -> None:
  n = len(nums)
  if n<=1:
    return None
  nums_sum = sum(nums)
  if not nums_sum%2==0:
    return None
  return try_partition_helper(nums[1:], [nums[0]], nums_sum//2-nums[0])

def try_partition_helper(nums: list[int], left: list[int], subset_sum_target: int):
  if subset_sum_target<0:
    return None
  if subset_sum_target==0:
    return (left, nums)
  return try_partition_helper(nums[1:], left + [nums[0]], subset_sum_target-nums[0])

# tests :
def test_dummy():
  assert True

def test_equal_sum_empty_array():
  subsets=try_partition([])
  assert subsets is None

def test_equal_sum_1_elem_array():
  subsets=try_partition([1])
  assert subsets is None

def test_equal_sum_2_equal_elem_array():
  subsets=try_partition([1, 1])
  assert subsets==([1], [1])

def test_equal_sum_3_equal_elem_array():
  subsets=try_partition([1, 1, 1])
  assert subsets is None

def test_equal_sum_4_equal_elem_array():
  subsets=try_partition([1, 1, 1, 1])
  assert subsets==([1, 1], [1, 1])

def test_equal_sum_3_diff_elem_array():
  subsets=try_partition([2, 1, 1])
  assert subsets==([2], [1, 1])

def hid_test_equal_sum():
  subsets=try_partition([1,5,11,5])
  assert subsets==([1, 5, 5], [11])

def test_no_equal_sum():
  subsets=try_partition([1,2,3,5])
  assert subsets is None


