"""
Coin Change 2 :
You are given an integer array coins representing coins of 
different denominations and an integer amount representing a 
total amount of money.
Return the number of combinations that make up that amount. 
If that amount of money cannot be made up by any 
combination of the coins, return 0. You may assume that you 
have an infinite number of each kind of coin. 
"""
def combinations(coins: list[int], amount: int) -> list[list[int]]:
  return combinations_helper(coins, amount, list())

def combinations_helper(coins: list[int], amount: int, comb_so_far: list[list[int]]) -> list[list[int]]:
  if amount<0 or len(coins)==0:
    return list()
  if amount==0:
    return comb_so_far
  if len(comb_so_far)==0:
    case1_comb_so_far=[[coins[0]]]
  else:
    case1_comb_so_far = [l+[coins[0]] for l in comb_so_far]
  case1 = combinations_helper(coins, amount-coins[0], case1_comb_so_far)
  case2 = combinations_helper(coins[1:], amount, comb_so_far)
  return case1 + case2

# tests :
def test_dummy():
  assert True

def test_coins_changes_not_empty_coins_array_0_amount():
  comb = combinations([1, 2, 3], 0)
  assert len(comb)==0

def test_coins_changes_empty_coins_array_0_amount():
  comb = combinations([], 0)
  assert len(comb)==0

def test_coins_changes_empty_coins_array():
  comb = combinations([], 12)
  assert len(comb)==0

def test_coins_changes_2_coins_array():
  comb = combinations([1, 2], 2)
  assert len(comb)==2

def test_coins_changes_1_coins_array_amount_less():
  comb = combinations([5], 2)
  assert len(comb)==0

def test_coins_changes_2_coins_array_no_combinations():
  comb = combinations([3, 5], 7)
  assert len(comb)==0

def test_coins_changes_2_coins_array():
  comb = combinations([1, 2], 3)
  assert len(comb)==2

def test_coins_changes_amount_ok():
  comb = combinations([1,2,5], 5)
  assert len(comb)==4

def test_coins_changes_amount_ok():
  comb = combinations([1,2,5], 11)
  assert len(comb)==11

def test_coins_changes_amount_ko():
  comb = combinations([2], 3)
  assert len(comb)==0
