# Recursion
1. When a function calls itself -- that's recursion.
2. There should be at least two execution paths through a recursive function:
   1. recursive case
   2. base case (function does not call itself)

Examples of recusion:
1. [Factorial](https://en.wikipedia.org/wiki/Factorial)
   1. factorial(1) = 1
   2. factorial(n) = n*factorial(n-1)
2. [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number)
   1. Fib(0) = 0
   1. Fib(1) = 1
   2. Fib(n) = Fib(n-1) + Fib(n-2)
3. [Flood Fill](https://en.wikipedia.org/wiki/Flood_fill)

    

## References
1. https://stackoverflow.com/questions/59833738/how-can-i-avoid-exceeding-the-max-call-stack-size-during-a-flood-fill-algorithm
1. http://inventwithpython.com/blog/2011/08/11/recursion-explained-with-the-flood-fill-algorithm-and-zombies-and-cats/
