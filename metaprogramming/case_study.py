class MetaClass(type):
    def __new__(cls, name, bases, attrs):
        # 在创建类时动态添加一个新方法
        attrs['new_method'] = lambda self: print("New method added!")
        
        return super().__new__(cls, name, bases, attrs)

# 使用元类创建类
class MyClass(metaclass=MetaClass):
    def existing_method(self):
        print("Existing method called.")

# 创建类的实例
obj = MyClass()
obj.existing_method() # 输出：Existing method called.
obj.new_method() # 输出：New method added!