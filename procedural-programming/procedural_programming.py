# 过程1:获取用户输入
def get_user_input():
    user_input = input("请输入您的名字：")
    return user_input

# 过程2:处理用户输入
def process_user_input(input_value):
    greeting = "您好，" + input_value + "!"
    print(greeting)

# 过程3:主程序
def main():
    user = get_user_input()
    process_user_input(user)

# 调用主程序
main()