
def factorial(n):
  if n == 1: return 1
  return n * factorial(n-1)

def test_factorial():
  assert 6 == factorial(3)
  assert 24 == factorial(4)
  assert 120 == factorial(5) 


