# 本篇我们学习一个特别的内容  提示和传递 相关重要知识点 为用户提示符设置变量
# 时间 2020/05/19 02:27
# 肥猫喜欢...特洛朱

from sys import argv
# 引入Python模块（引入模块后命令行运行需要参数 参数数量取决于解包变量数量）

script, User_name, User_live = argv
# 将参数赋予变量值
prompt = '--'
# 将‘--’赋予变量值prompt

print(f"Hi, {User_name}, I'm the {script} script!")
# 使用 .format("{...}") 嵌入格式化字符串方法输出字符串
print("I'd like ask you a few questions.")
# 日常输出字符串
print(f"Do you like me {User_name}?")
# 使用 .format("{...}") 嵌入格式化字符串方法输出字符串
likes = input(prompt)
# 键盘输入变量值赋予变量

print(f"Where do you live {User_live}?")
# 使用 .format("{...}") 嵌入格式化字符串方法输出字符串
live = input(prompt)
# 键盘输入变量值赋予变量

print("what kind of computer do you have?")
#日常输出字符串
computer = input(prompt)
# 键盘输入变量值赋予变量

print(f"""
Alright! So you said {likes} about liking me.
Your living {User_live}. Not sure where that is.
And you have a {computer} computer, Nice!
""")
# 日常.format(f"{...}")加多段输出
