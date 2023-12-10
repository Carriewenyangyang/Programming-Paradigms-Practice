import multiprocessing
# 依赖关系较强的循环
def complex_calculation(nums):
    result = 0
    for num in nums:
        # 模拟一个复杂的计算，该计算依赖前一个数的结果
        result = result + num**2 + result
    
    return result

if __name__ == "__main__":
    # 输入数组
    numbers = list(range(1, 1000001))
    
    # 使用两个进程分别计算复杂计算的结果
    with multiprocessing.Pool(2) as pool:
        result = sum(pool.map(complex_calculation, [numbers]))

    print("Result:", result)