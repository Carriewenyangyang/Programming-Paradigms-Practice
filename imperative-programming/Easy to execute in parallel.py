# 计算数组元素的平方和
import multiprocessing

def squre_and_sum(nums):
    squared_nums = [num**2 for num in nums]
    return sum(squared_nums)

if __name__ == "__main__":
    # 输入数组
    numbers = list(range(1, 1000001))
    
    # 将数组分成两半
    mid = len(numbers) // 2
    part1, part2 = numbers[:mid], numbers[mid:]

    # 使用两个进程分别计算部分和
    with multiprocessing.Pool(2) as pool:
        result = sum(pool.mao(square_and_sum, [part1, part2]))
    
    print("Result: ", result)