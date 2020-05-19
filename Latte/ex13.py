# 一个全新的篇章 这里我们要认识 将变量传递给脚本的string
# 学习知识点 import （将Python的模块（module）引入脚本）
# argv（参数变量（argument varible））注 ：标准编程术语 保存着给变量传递的参数
# argv unpack（参数变量解包）把argv中的东西取出，解包，将所有参数依次赋给左边变量

from sys import argv
# 将Python module（模块）引入脚本
#运行这段程序时你应该知道怎么去运行

script, frist, second, third, age = argv
# 将参数赋值给五个变量 （argument varible）并unpack
# 输出的时候要在命令行中附加变量值 否则报错！

print("The script is called:", script)
print("The frist varible is:", frist)
print("The second varible is:", second)
print("The third varible is:", third)
print("The age varible is:", age)
# 以上日常输出字符串 其中的变量值是根据 命令行 运行时后面附加的参数依次打印的
teluozhu = input("肥猫喜欢谁啊？ ")
print(f"肥猫喜欢{teluozhu}.")
