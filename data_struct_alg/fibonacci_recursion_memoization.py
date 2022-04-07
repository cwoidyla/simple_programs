

'''
Goal: recursively find the specified fibonacci number

inputs: numbers
datatype? integers
max = 100
min = 0

output: entire sequence
datatype: integer

performant?
should execute in less than 1 sec

fibonacci sequence
0,1,1,2,3,5,8,13,21,34,55...
'''

import unittest
import time

class FibonacciTest(unittest.TestCase):
  def test_mid_bound(self):
    self.fib0 = Fibonacci(5)
    answer = [0, 1, 1, 2, 3, 5]
    output = self.fib0.calculate()
    self.assertEqual(answer, output)
    self.fib0 = Fibonacci(10)
    answer = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    output = self.fib0.calculate()
    self.assertEqual(answer, output)

  def test_upper_bound(self):
    self.fib1 = Fibonacci(10)
    answer = self.fib1.calculate()
    output = self.fib1.calculate()
    self.assertEqual(answer, output)

  def test_lower_bound(self):
    self.fib2 = Fibonacci(0)
    answer = [0]
    output = self.fib2.calculate()
    self.assertEqual(answer, output)
    self.fib2.fib_num = 1
    answer = [0, 1]
    output = self.fib2.calculate()
    self.assertEqual(answer, output)
    self.fib2.fib_num = 2
    answer = [0, 1, 1]
    output = self.fib2.calculate()
    self.assertEqual(answer, output)

  def test_time(self):
    start = time.time()
    self.fib3 = Fibonacci(0)
    for i in range(900, 0, -1):
      self.fib3.fib_num = i
      self.fib3.calculate()
    end = time.time()
    total = end - start
    print("total time to execute 100 iterations is {}".format(total))
    self.assertLess(total, 1.0)

class Fibonacci:
  def __init__(self, fib_num):
    self.fib_num = fib_num
    self.fib_mem = [0, 1]

  def calculate(self):
    if self.fib_num == 0:
      return [0]
    if self.fib_num == 1:
      return [0, 1]
    # Memoization implementation
    if len(self.fib_mem) > self.fib_num:
      fib_ans = self.fib_mem[:self.fib_num + 1] 
      return fib_ans
    seeds = [0, 1, 1]
    fib_ans = self._recurse_calc(self.fib_num - 2, seeds)
    if len(fib_ans) > len(self.fib_mem):
      self.fib_mem = fib_ans
    return fib_ans

  def _recurse_calc(self, lvl, num):
    if lvl != 0:
      num += [num[-1] + num[-2]]
      lvl -= 1
      num = self._recurse_calc(lvl, num)
    return num


if __name__ == '__main__':
  unittest.TestCase()




