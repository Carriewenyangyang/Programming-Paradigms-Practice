# finonacci
def fibonacci(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
        
    return b

result = fibonacci(5)
print(result) # 输出5