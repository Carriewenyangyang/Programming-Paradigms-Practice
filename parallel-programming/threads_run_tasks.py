import threading
import time

def task(name):
    for i in range(5):
        print(f"Thread {name}: Task {i}")
        time.sleep(1)

# 创建两个线程
thread1 = threading.Thread(target=task, args=("A",))
thread2 = threading.Thread(target=task, args=("B",))

# 启动线程
thread1.start()
thread2.start()

# 等待两个线程执行完成
thread1.join()
thread2.join()

print("Main Thread: All tasks completed.")
