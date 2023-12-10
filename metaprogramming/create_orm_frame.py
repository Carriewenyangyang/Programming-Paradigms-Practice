# 假设有一个用于执行SQL语句的函数
def execute_sql(sql):
    # 实际上这里应该有连接数据库、执行SQL等操作，这里简化为打印SQL语句
    print(f"Executing SQL: {sql}")

class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['table_name'] = name.lower() + "s"
        create_table(attrs['table_name'])
        return super().__new__(cls, name, bases, attrs)

def create_table(table_name):
    # 实际上这里应该有创建数据库表的操作，这里简化为打印信息
    print(f"Creating table: {table_name}")

class Model(metaclass=ModelMeta):
    def save(self):
        # 构造插入语句
        fields = ', '.join(f"'{value}'" for value in self.__dict__.values())
        columns = ', '.join(self.__dict__.keys())
        sql = f"INSERT INTO {self.table_name} ({columns}) VALUES ({fields})"
        
        # 执行插入语句
        execute_sql(sql)

# 创建模型类
class User(Model):
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 使用模型类
user = User(name="John", age=25)
user.save()
