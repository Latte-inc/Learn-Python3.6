# This is Exercises for ex10.py .
# Time 2020/05/17 02:21
# fatcat like teluozhu

latte = "\tLatte is coffee!"
# 变量赋值
Mylove = "\tteluozhu"
# 变量赋值
fatcat = "only"
# 变量赋值
fat_cat = """
\tMy love
\tis teluozhu
\tfatcat very like teluozhu
"""
# 变量赋值
print(f"\tWho is my love {Mylove}")
# 输出字符串 使用 f"{}" 格式化字符嵌入 string
print("\tWhat's Latte?", latte.format(latte))
# 输出字符串 使用 .format(...) string输出格式化字符 （其中使用了函数方法 变量名.format（变量名））
# 返回 latte 变量到其它字符中
print("I wish :", fat_cat)
# 输出字符串
