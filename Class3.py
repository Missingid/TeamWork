# while循环（满足条件时进入循环）
"""current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1"""

"""prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. " 
message = "" 
while message != 'quit':     
    message = input(prompt)     
    print(message)"""

# break和continue
# break：从循环出来结束循环
# continue：跳过此次循环，进入下一循环
"""prompt="\nPlease enter the name of a city you have visited:"
prompt+="\n(Enter 'quit' when you are finished.)"
while True:
    city=input(prompt)
    if city=='quit':
        break
    else:
        print("I'd love to go to"+city.title()+"!") 
        #title()函数返回标题化的字符串，即开头大写"""

"""current_number=0
while current_number<10:
    current_number+=1
    if current_number %2 ==0:
        continue
    print(current_number)"""

# for循环
## 遍历
"""for letter in 'Python':     # 第一个实例
   print("当前字母: %s" % letter)
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print ('当前水果: %s'% fruit)
 
print ("Good bye!")"""

## 通过序列索引迭代
"""fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('当前水果 : %s' % fruits[index])
 
print ("Good bye!")"""

# 函数
## 函数定义
"""def greet_user(name): #greet_user()函数名 name：函数的输入，只是形参，可以随意命名
    print("Hello,"+name.title()+"!") #函数里的操作

## 调用函数
greet_user("Jesse") #Jesse是实参"""
###编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，Python将使用指定的实参值；
###否则，将使用形参的默认值。因此，给形参指定默认值后，可在函数调用中省略相应的实参。

## 函数返回值
"""def calculate(number):
    return(number+1)

print(calculate(1))"""

"""import Class3_pizza #导入含有make_pizza函数定义的py文件Class3_pizza
Class3_pizza.make_pizza(12, 'mushrooms', 'green peppers') #调用函数"""