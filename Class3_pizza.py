def make_pizza(size, *toppings):     
    #形参名*toppings中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
    """概述要制作的比萨"""     
    print("\nMaking a " + str(size) +"-inch pizza with the following toppings:")     
    for topping in toppings:         
        print("- " + topping) 