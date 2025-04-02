def double_it(n):
    result=n*n
    print(result)
double_it(10)

# function default return None
print("double is : ",double_it(10))

def sum(a,b):
    return a+b
print("sum is :",sum(10,20))

# default parameter

def default_par(val="default value"):
    print(val)
default_par("my custom par")
default_par()

# Arbitrary Arguments, *args

def arbitrary_arguments(*kids):
    print(kids[2])
arbitrary_arguments("jony","sony","rony")

def arbitrary_arguments_2(a_1,a_2,*kids):
    print(a_1,a_2)
    for p in kids:
        print(p)

arbitrary_arguments_2("jony","sony","rony","jemy","hasi")

# Keyword Arguments
def keyword_arguments(child1,child2):
    print(child1)
    print(child2)
keyword_arguments(child2="ch2",child1="ch1")

# Arbitrary Keyword Arguments, **kwargs

def kwargs(**kids):
    for key,value in kids.items():
        print(key,value)
kwargs(p_1="pagol",p_2="sagol")

# multiple return
def multiple_return(num_1,num_2):
    sum=num_1+num_2
    mult=num_2*num_2
    rem=num_2-num_1

    # return sum,mult,rem
    return [sum,mult,rem]
print(multiple_return(10,20))