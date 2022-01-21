"""编写类时，你定义一大类对象都有的通用行为。
基于类创建对象时，每个对象都自动具备这种通用行为，然后可根据需要赋予每个对象独特的个性。"""
#类的定义
class Dog(): 
    """一次模拟小狗的简单尝试"""   
    def __init__(self, name, age):       
        """初始化定义 Python调用__init__()来创建Dog实例时，将自动传入实参self，self就指的是实例。"""  
        """初始化属性name和age"""          
        self.name = name         
        self.age = age    
    def sit(self):         
        """模拟小狗被命令时蹲下"""         
        print(self.name.title() + " is now sitting.")     
    def roll_over(self):         
        """模拟小狗被命令时打滚"""         
        print(self.name.title() + " rolled over!") 
#实例化：根据类创建对象
my_dog = Dog('willie', 6) #Dog是类的名字 函数参数是init函数对应的参数 Dog类创建的实例被保存在my_dog中
##访问属性
print(my_dog.name)
print(my_dog.age)
##调用方法
my_dog.sit()
my_dog.roll_over()
##属性不作为类的参数
class Car():     
    def __init__(self, make, model, year):         
        """初始化描述汽车的属性"""         
        self.make = make         
        self.model = model         
        self.year = year          
        self.odometer_reading = 0     #odomerter_reading属性并没有出现在init参数中
    def get_descriptive_name(self):         
        """返回整洁的描述性信息"""         
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model         
        return long_name.title()   
    def update_odometer(self, mileage):         
        """将里程表读数设置为指定的值"""         
        self.odometer_reading = mileage  
    def read_odometer(self):         
        """打印一条指出汽车里程的消息"""         
        print("This car has " + str(self.odometer_reading) + " miles on it.") 
my_new_car = Car('audi', 'a4', 2016) 
print(my_new_car.get_descriptive_name()) 
my_new_car.update_odometer(23) 
my_new_car.read_odometer() 

#继承
"""一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；
原有的类称为父类，而新类称为子类。
子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。"""
##ElectricCar类继承Car类，并添加新属性battery_size
class ElectricCar(Car):        
    def __init__(self, make, model, year):         
        """先初始化父类的属性，再初始化电动汽车特有的属性"""       
        super().__init__(make, model, year) #父类也称超类，所以用super指代
        self.battery_size = 70      
    def describe_battery(self):         
        """打印一条描述电瓶容量的消息"""         
        print("This car has a " + str(self.battery_size) + "-kWh battery.") 

my_tesla = ElectricCar('tesla', 'model s', 2016) 
print(my_tesla.get_descriptive_name()) 
my_tesla.describe_battery()

##重载
"""对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。
为此，可在子类中定义一个这样的方法，即它与要重写的父类方法同名。
这样，Python将不会考虑这个父类方法，而只关注你在子类中定义的相应方法。"""
class ElectricCar2(ElectricCar):        
    def __init__(self, make, model, year):         
        """先初始化父类的属性，再初始化电动汽车特有的属性"""       
        super().__init__(make, model, year) #父类也称超类，所以用super指代
        self.battery_size = 80      
    def describe_battery(self):         
        """打印一条描述电瓶容量的消息"""         
        print("This ElectricCar has a " + str(self.battery_size) + "-kWh battery.") 

my_tesla2 = ElectricCar2('tesla', 'model s', 2016) 
my_tesla2.describe_battery()

##ElectricCar同时继承Car类和Battery类

