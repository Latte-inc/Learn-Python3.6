# This is learn Python new string ! function ready now!
# Time 2020/05/17 00:32
# fatcat like .....

formatter = "{} {} {} {}"
# 给变量 formatter 赋值

print(formatter.format(1,2,3,4))
# 打印字符串 其中使用方法 function string （函数）
# formatter.format（...）使用函数让它返回 formatter 变量到其它字符中。
print(formatter.format("one", "two", "three", "four"))
# 同上 但是此处嵌入变量不是空值，所以变量值 formatter 的字符串被替代掉
print(formatter.format(True, False, False, True))
# 同上 其中 True False 为布尔值 在Python语言中为真 假判断
print(formatter.format(formatter, formatter, formatter, formatter))
# 同上 但是此处嵌入变量值为 formatter
print(formatter.format(
      "Try your",
      "Own text here",
      "Maybe a poem",
      "Or a song about fear"
))
# 同上 使用 .format(...) string 输出字符
