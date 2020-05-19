# 这里是肥猫的练习章节，在这里使用模块（module）方法以及 input方法 和给标识符赋值
# 时间 2020/05/19 16:48
# 肥猫喜欢...特洛朱

from sys import argv

script, User_name, User_key, Admin_one = argv
prompt = '###Latte>'

print(f"Welcome to Latte and fatcat code servers!{Admin_one}")
print("\t服务从这里开始为中文！")
print("\t请输入你的用户名：")
name = input(prompt)

print("\t请输入你的秘钥：")
key = input(prompt)

print(f"""
\t*欢迎尊敬的用户{name}登录服务系统。
\t*由于您的密码 {key} 安全性过低！请您更换密码！
\t*此段演示代码使用了{User_name} {User_key} 方法。
""")
