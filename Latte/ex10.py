# What's this？  New learn Exercises.  new line character(\n) 换行字符
# Time 2020/05/17 01:21
# fatcat like ...

tabby_cat = "\tI'm tabbed in."
# 变量赋值 其中值 \t 为 ASCII 水平制表符
persian_cat = "I'm split\non aline."
# 变量赋值 其中 \n 为 ASCII 换行符
backslash_cat = "I'm \\ a \\ cat."
# 变量赋值 其中 \\ 为反斜杠 输出显示 \

fat_cat = """
I'll do a list:
\t* Cat_food
\t* Fishies
\t* Catnip\n\t* Grass
\t* fatcat like ... teluozhu
"""
# 变量 fat_cat 赋值 使用三段双引号 """ 输出多行字符 其中 \t 为 ASCII 水平制表符
# \n\t表示 ASCII 换行并水平（TAB）
fatcat = "I am 6'2\" tall."
# 将字符中的双引号转义
fatcat1 = 'I am 6\'2" tall.'
# 将字符中的单引号转义

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(fatcat)
print(fatcat1)
# 日常输出字符串...
