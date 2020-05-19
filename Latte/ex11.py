# 这是一个新的篇章 ， 肥猫以后的注释将会使用中文 ， 包括程序注释头。
# 本片开始学习Python的输入 （input）
# 时间 2020/05/19 00:08
# 肥猫喜欢。。。特洛

print("How old are you?", end=' ')
# 输出字符串 使用 end=' '结尾，防止换行符换行
age = input()
# 变量赋值 input() 从键盘获取值
print("How tall are you?", end=' ')
# 输出字符串 使用 end=' '结尾，防止换行符换行
height = input()
# 变量赋值 input() 从键盘获取值
print("How much are you weight?", end=' ')
# 输出字符串 使用 end=' '结尾，防止换行符换行
weight = input()
# 变量赋值 input() 从键盘获取值

print(f"So, your {age} old, {height} tall and {weight} heavy.")
# 日常输出  使用 format(f"..{}..") string输出嵌入格式化字符
