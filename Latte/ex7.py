# This is ex1.py-ex6.py Exercises.
# print string . variable string . format{} string . .format() string
# Time 2020/05/16 00:42
# Fatcat like...

print("Marry had a little lamb.")
# 打印双引号内的字符串
print("Its fleece was white as {}.".format('snow'))
# 打印双引号内的字符串，其中 .format() 方法中括号内单引号为输出字符 'snow'不是变量
print("And everywhere that Mary went.")
# 打印双引号内的字符串
print("." * 10)
# 打印双引号内的字符串，其中 "."为正常字符串打印 * 10 为将此字符输出10个一样字符。

end1 = "c"
# 变量赋值
end2 = "h"
# 变量赋值
end3 = "e"
# 变量赋值
end4 = "e"
# 变量赋值
end5 = "s"
# 变量赋值
end6 = "e"
# 变量赋值
end7 = "B"
# 变量赋值
end8 = "u"
# 变量赋值
end9 = "r"
# 变量赋值
end10 = "g"
# 变量赋值
end11 = "e"
# 变量赋值
end12 = "r"
# 变量赋值

# 删除后面的逗号及逗号后内容，看看会发生什么！
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
# 打印字符串 字符拼接 其中 , end='' 表示在循环中不换行 ！
print(end7 + end8 + end9 + end10 + end11 + end12)
# 打印字符串 字符串拼接
