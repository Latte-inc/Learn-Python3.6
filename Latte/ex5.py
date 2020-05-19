# # This code is learn Python new code, variable format string start!
# Time 2020/05/15 00:44
# fatcat like .....

my_name = 'fatcat'
my_age = 24 #肥猫真的24岁哦！
my_height = 176 #是厘米（CM）哦！
my_weight = 93 #是公斤（Kg）哦！
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'

#上述变量被赋予了两种类型 一种是赋予变量数字值，一种是赋予变量字符串。

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} CM.")
print(f"He's {my_weight} kilo.")
print("Actually that's not too heavy.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky , try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

# 上述代码（15-23 line）使用了 格式化字符串（format string） 并在字符串里嵌入变量
# 所使用的的方法为 print（f“｛｝”），在双引号前加入 f 相当于告诉编译器这是个格式化字符
