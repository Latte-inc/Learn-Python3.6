# 类似于ex11.py 换一种带有提示的方式来输入字符串并输出
# 时间 2020/05/19 00:42
# 肥猫喜欢...特洛朱

age = input("How old are you? ")
# 变量赋值 input（"..."）string 可以简化ex11.py写法
height = input("How tall are you? ")
# 同上
weight = input("How much do you weight? ")
# 同上

print(f"So, your {age} old, {height} tall and {weight} heavy.")
# 日常输出  使用 format(f"..{}..") string输出嵌入格式化字符
