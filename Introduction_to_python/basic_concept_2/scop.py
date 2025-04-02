
global_var_1=5000
global_var_2="I phone 15 Pro"

def my_func(price):
    global global_var_1

    global_var_1=global_var_1-price
    my_name="Majharul"
    print(f"I am {my_name},I want to by {global_var_2},my balance after buy {global_var_1}")
my_func(1000)


# print(my_name)


'''
1.can not access function local variable outside of functon
2.can access global variable inside function
3.if want to change global variable value need to use global keyword

'''