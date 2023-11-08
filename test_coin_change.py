"""
Coin Change :
You are given an integer array coins representing coins of 
different denominations and an integer amount representing a 
total amount of money. 
Return the fewest number of coins that you need to make up 
that amount. If that amount of money cannot be made up by 
any combination of the coins, return -1. You may assume that 
you have an infinite number of each kind of coin.
"""
def fewest_nbr_coins(coins: list[int], amount: int) -> int:
  return fewest_nbr_coins_helper(coins, amount, 0)

def fewest_nbr_coins_helper(coins: list[int], amount: int, coins_nbr: int) -> int:
  if len(coins)==0:
    return -1
  if amount==0:
    return coins_nbr
  if amount<0:
    return -1
  case1 = fewest_nbr_coins_helper(coins, amount-coins[0], coins_nbr + 1)
  case2 = fewest_nbr_coins_helper(coins[1:], amount, coins_nbr)
  if case1!=-1 and case2 != -1:
    return min(case1, case2)
  elif case1==-1:
    return case2
  else:
    return case1

# tests :
def test_dummy():
  assert True

def test_coins_changes_not_empty_coins_array_0_amount():
  assert fewest_nbr_coins([1, 2, 3], 0)==0

def test_coins_changes_empty_coins_array_0_amount():
  assert fewest_nbr_coins([], 0)==-1

def test_coins_changes_empty_coins_array():
  assert fewest_nbr_coins([], 12)==-1

def test_coins_changes_2_coins_array():
  assert fewest_nbr_coins([1, 2], 2)==1

def test_coins_changes_2_coins_array():
  assert fewest_nbr_coins([1, 2], 3)==2

def test_coins_changes_1_coins_array_amount_less():
  assert fewest_nbr_coins([5], 2)==-1

def test_coins_changes_2_coins_array_no_combinations():
  assert fewest_nbr_coins([3, 5], 7)==-1

def test_coins_changes_amount_ok():
  nbr_coins = fewest_nbr_coins([1,2,5], 11)
  assert nbr_coins==3

def test_coins_changes_amount_ko():
  nbr_coins = fewest_nbr_coins([2], 3)
  assert nbr_coins==-1
