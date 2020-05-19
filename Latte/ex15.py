# 这个练习是比较重要的，在这里我们将学到新的方法 读取文件
# 知识点涉及 函数 read（读取） open（打开）
# 时间 2020/05/19 17:31
# 一厢情愿，有始无终

from sys import argv
# 通俗点就是将 sys 软件包中的 模块（module）引入脚本

script, filename = argv
# 将参数赋予变量值
txt = open(filename,encoding='utf-8')
#  这里使用了函数 open(name,encoding='..')来打开文件
# 此处是个很重要的知识点 当编译器报错提示 Unicode ERROR XXXX...
# 一定open（filename,encoding='编码方式'） 要告诉编译器编码类型 不然报错！！
# 虽然这样写多一个单词  但是能将Bug解决。

print(f"Here's your file {filename}:")
# 日常输出 使用方法 .format(f"{...}") 输出嵌入格式化字符串
print(txt.read())
# 虽然是输出  但是这里使用了函数 read 方法 (txt.read()) 相当于执行读取并输出

print("Type a filename again:")
file_again = input('>')

txt_again = open(file_again,encoding='utf-8')

print(txt_again.read())
