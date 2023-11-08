"""
Decode Ways :
A message containing letters from A-Z can be encoded into 
numbers using the following mapping: 
'A' -> "1", 'B' -> "2", ..., 'Z' -> "26"

For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot 
be mapped into 'F' since "6" is different from "06". Given a string 
s containing only digits, return the number of ways to decode 
it.
"""
ALPH = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
MAP = dict([ (str(i), a) for i, a in zip(range(1, 27), ALPH)])

def decode_nbr_ways(s: str) -> int:
  pass

# tests :
def test_dummy():
  assert True

def hid_test_decode_ok():
  nbr = decode_nbr_ways("12")
  assert nbr==2
