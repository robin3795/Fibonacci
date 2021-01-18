from time import time, sleep
import Fibonacci

def timestamp():
    start = time()
    def duration ():
        return time() - start
    return duration

def func_to_str(function_name):
    str_function = str(function_name)
#    print (str_function) ##<function fib_iteration at 0x00000200BD971CA8>
    return str_function.split(' ')[1]

def run_fibonacci_func(func, par_list):
    then = timestamp()
    n = par_list[0]
    par_str = str(n)
    if len(par_list) == 1:
        print (func(n))
        print ("%1.8f seconds " %then() + "for " + func_to_str(func) + "(" + str(n) +")" )
    if len(par_list) == 2:
        print (func(n, par_list[1]))
        print ("%1.8f seconds " %then() + "for " + func_to_str(func) + "(" + str(n) +")" )
            

##then = timestamp()
##n = 40
##print (Fibonacci.fib_iteration(n))
##print ("%1.8f seconds " %then() + "for fib_iteration(" + str(n) +")" )
    
functions = [[Fibonacci.fib_iteration, 40]
             ,[Fibonacci.fib_recursion, 20]
             ,[Fibonacci.fib_recursion18, 20]
             ,[Fibonacci.fib_lookuptable, 40, {1:1, 2:1}]
             ,[Fibonacci.fib_Dictionary,40]
             ]
for each_func in functions:
    run_fibonacci_func(each_func[0], each_func[1:])
           
                       

