"""
Min cost for tickets:
You have planned some train traveling one year in advance. The 
days of the year in which you will travel are given as an integer 
array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:
- a 1-day pass is sold for costs[0] dollars,
- a 7-day pass is sold for costs[1] dollars, and
- a 30-day pass is sold for costs[2] dollars.

The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel 
for 7 days: 2, 3, 4, 5, 6, 7, and 8. Return the minimum number of 
dollars you need to travel every day in the given list of days.

"""
COSTS = [2,7,15]
def min_cost_ticket(days: list[int]) -> int:
  n = len(days)
  if n==0:
    return 0
  cost = COSTS[0] * n
  if cost > COSTS[1]:
    case1 = COSTS[1] + min_cost_ticket(remove_days_up_to(days, 7))
    case2 = COSTS[2] + min_cost_ticket(remove_days_up_to(days, 30))
    print([days, (case1, case2)])
    return min(case1, case2)
  
  return cost

def remove_days_up_to(days: list[int], up_to: int) -> list[int]:
  if len(days)==0:
    return []
  first = days[0]
  while len(days)>0 and (days[0]-first<up_to):
    days = days[1:]
  return days

# tests :
def test_dummy():
  assert True

def test_remove_days_up_to_empty_days_array():
  assert remove_days_up_to([], 7)==[]

def test_remove_days_up_to_7_days_array():
  assert remove_days_up_to([1, 6], 7)==[]
  assert remove_days_up_to([1, 7], 7)==[]

def test_remove_days_up_to_8_days_array():
  assert remove_days_up_to([1, 7, 8], 7)==[8]
  assert remove_days_up_to([1, 6, 8], 7)==[8]

def test_min_cost_0_day():
  assert min_cost_ticket([])==0

def test_min_cost_1_day():
  assert min_cost_ticket([1])==2

def test_min_cost_2_consecutif_days():
  assert min_cost_ticket([1, 2])==4

def test_min_cost_3_consecutif_days():
  assert min_cost_ticket([1, 2, 3])==6

def test_min_cost_4_consecutif_days():
  assert min_cost_ticket([1, 2, 3, 4])==7

def test_min_cost_5_consecutif_days():
  assert min_cost_ticket([1, 2, 3, 4, 5])==7

def test_min_cost_7_consecutif_days():
  assert min_cost_ticket([1, 2, 3, 4, 5, 6, 7])==7

def test_min_cost_8_consecutif_days():
  assert min_cost_ticket([1, 2, 3, 4, 5, 6, 7, 8])==9 #7 + 2

def test_min_cost_2_consecutif_weeks_ranges():
  """
  [1,2,3,6,7] => 7$
  [8]         => 2$
  """
  assert min_cost_ticket([1, 2, 3, 6, 7, 8])==9

def test_min_cost_3_consecutif_weeks_ranges():
  """
  [1,2,3,6,7]   => 7$
  [8,9,10, 11]  => 7$
  [15, 16]      => 4$
  """
  assert min_cost_ticket([1, 2, 3, 6, 7, 8, 9, 10, 11, 15, 16])==15

def test_min_cost_3_weeks_ranges():
  """
  [1,2,3,6,7]   => 7$
  [8,9,10, 11]  => 7$
  [33, 34]      => 4$
  """
  assert min_cost_ticket([1, 2, 3, 6, 7, 8, 9, 10, 11, 33, 34])==18

def test_min_cost_1_week_then_1_day_per_week_case_1():
  """
  [1,2,3,6,7] => 7$
  [8]         => 2$
  [15]        => 2$
  """
  assert min_cost_ticket([1, 2, 3, 6, 7, 8, 15])==11

def test_min_cost_1_week_then_1_day_per_week_case_2():
  """
  [1,4,6,7] => 7$
  [8]       => 2$
  [20]      => 2$
  ==============
            => 11$
  """
  assert min_cost_ticket([1,4,6,7,8,20])==11

def test_min_cost_3_weeks():
  """
  [1,2,3,4,5,6,7]             => 7$
  [8,14]                      => 7$
  [15,16,17,20]               => 7$
  [33]                        => 2$
  ===21$===BUT GOOD CHOICE IS==17$===
  [1,2,3,4,5,6,7,8,14,15,20]  => 15$
  [33]                        => 2$
  """
  assert min_cost_ticket([1,2,3,4,5,6,7,8,14,15,16,17,20,33])==17




