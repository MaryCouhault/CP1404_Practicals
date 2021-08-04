"""
Author: Mary Couhault
Date: 10/04/21
Description:
Warm up Practice for List Practical
"""
"""
numbers[0]
numbers[-1]
numbers[3]
numbers[:-1]
numbers[3:4]
5 in numbers
7 in numbers
"3" in numbers
numbers + [6, 5, 3]
---
3
2
1
[3, 1, 4, 1, 5, 9]
[1]
True
False
False
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""
from operator import itemgetter

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers2 = [6, 5, 3]
numbers.extend(numbers2)
numbers[-1] = 1

print(numbers)
print(numbers[:-2])

numbers.sort(key=itemgetter(1))
number_of_elements = len(numbers)
print(number_of_elements)