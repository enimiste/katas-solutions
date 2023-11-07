"""
Climbing Stairs :
You are climbing a staircase. It takes n steps to reach the top. 
Each time you can either climb 1 or 2 steps. In how many 
distinct ways can you climb to the top?
"""
def climbing_stairs_ways(nstairs: int) -> int:
  if nstairs<=3:
    return nstairs
  return climbing_stairs_ways(nstairs-1) + climbing_stairs_ways(nstairs-2)

# tests :
def test_dummy():
  assert True

def test_when_0_stairs_should_return_0_ways():
  """
  0 step
  """
  ways = climbing_stairs_ways(0)
  assert ways==0

def test_when_1_stairs_should_return_1_ways():
  """
  1 step
  """
  ways = climbing_stairs_ways(1)
  assert ways==1

def test_when_2_stairs_should_return_2_ways():
  """
  1 step + 1 step
  2 steps
  """
  ways = climbing_stairs_ways(2)
  assert ways==2

def test_when_3_stairs_should_return_3_ways():
  """
  1 step + 1 step + 1 step
  1 step + 2 step
  2 step + 1 step
  """
  ways = climbing_stairs_ways(3)
  assert ways==3

def test_when_4_stairs_should_return_4_ways():
  """
  1 step + 1 step + 1 step + 1 step
  1 step + 1 step + 2 step
  2 step + 1 step + 1 step
  1 step + 2 step + 1 step
  2 step + 2 step
  """
  ways = climbing_stairs_ways(4)
  assert ways==5

def test_when_5_stairs_should_return_7_ways():
  """
  1 step + 1 step + 1 step + 1 step + 1 step
  1 step + 1 step + 1 step + 2 step
  1 step + 1 step + 2 step + 1 step
  2 step + 1 step + 1 step + 1 step
  2 step + 1 step + 2 step
  1 step + 2 step + 1 step + 1 step
  1 step + 2 step + 2 step
  2 step + 2 step + 1 step
  """
  ways = climbing_stairs_ways(5)
  assert ways==8

