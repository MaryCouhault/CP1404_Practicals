import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# The first lines smallest number is 5 and the largest it can generate is 20

# Line 2's largest number is 8 and the smallest it can generate is 3. NO it will not become 4
# as it skips for and goes to 5

# Line 3's smallest number is 2,6 and the largest is 5.4

print(random.randint(1,101))
