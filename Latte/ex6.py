# This is learn Python code new ! format string new .format() string
# Time 2020/05/16 00:02
# Fatcat like.....

types_of_people = 10  #给变量 types_of_people 赋值
x = f"There are {types_of_people} types_of_people."
# 给变量X赋值 使用 format｛｝ 方法 在字符串中嵌入变量

binary  = "binary"  # 给变量 binary 赋值 赋值为字符串
do_not = "don't"  #同上
y = f"Those who know {binary} and those who {do_not}."
# 给变量 y 赋值 使用 format｛｝ 方法 在字符串中嵌入变量

print(x)
print(y)
print(f"I said: {x}")
print(f"I also said: '{y}'")
#（14-15 line）直接打印变量值 x y
#（16-17 line）打印变量 使用 format｛｝方法打印字符串+字符串嵌入变量

hilarious = False # 给变量 hilarious 赋值布尔值 False 
joke_evaluation = "Isn't that joke so funny? {}!"
# 给变量 joke_evaluation 赋值 值为 字符串+format｛｝方法嵌入变量

print(joke_evaluation.format(hilarious))
#打印字符串 其中 .format() 方法为嵌入变量

w = "This is the life side of..."
# 给变量 W 赋值 赋值类型字符串
e = "a string is a right side."
# 给变量 e 赋值 赋值类型同上

print(w + e)  # 打印字符串拼接
