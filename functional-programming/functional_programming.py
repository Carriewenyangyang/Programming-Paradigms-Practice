from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Map: 对每个元素应用相同的操作
squared_numbers = list(map(lambda x: x**2, numbers))

# 加法
# Reduce: 将所有元素合并为一个结果
sum_of_squares = reduce(lambda x, y: x + y, squared_numbers)

print(sum_of_squares)

# 减法
# Reduce: 将所有元素合并为一个结果
result = reduce(lambda x, y: x - y, squared_numbers)

print(result)