from pyDatalog import pyDatalog

# 定义逻辑关系
pyDatalog.create_terms('father, mother, parent, grandparent')

# 规定家庭关系
+father('John', 'Jim')
+father('John', 'Ann')
+mother('Jane', 'Jim')
+mother('Jane', 'Ann')

# 规定父母关系
parent(X, Y) <= father(X, Y)
parent(X, Y) <= mother(X, Y)

# 规定祖父母关系
grandparent(X, Y) <= parent(X, Z) & parent(Z, Y)

# 查询家庭关系
print(grandparent('John', 'Ann'))
