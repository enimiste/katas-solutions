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
  if len(s)==0:
    return 1
  if len(s)==1:
    return 1 if s in MAP else 0
  
  if len(s)>=2:
    nbr=0
    if s[0] in MAP:
      nbr+=decode_nbr_ways(s[1:])
    if s[0:2] in MAP:
      nbr+=decode_nbr_ways(s[2:])
    return nbr
  return -1

# tests :
def test_dummy():
  assert True

def test_decode_empty_string():
  assert decode_nbr_ways('')==1

def test_decode_1_digit_string_less_1():
  assert decode_nbr_ways('0')==0

def test_decode_1_digit_string():
  assert decode_nbr_ways('1')==1
  
def test_decode_2_digits_string_less_than_26():
  """
  AB
  L
  """
  assert decode_nbr_ways('12')==2

def test_decode_2_digits_string_greater_than_26():
  """
  II
  """
  assert decode_nbr_ways('99')==1

def test_decode_3_digits_string_ok():
  """
  ABC
  LC
  AW
  """
  assert decode_nbr_ways('123')==3

def test_decode_4_digits_string_ok():
  """
  ABBC
  ABW
  LW
  LBC
  AVC
  """
  assert decode_nbr_ways('1223')==5

def test_decode_5_digits_string_ko():
  """
  AAJF
  KJF
  """
  assert decode_nbr_ways('11106')==2

