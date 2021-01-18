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

def run_fibonacci_func(func, n):
    then = timestamp()
    print (func(n))
    print ("%1.8f seconds " %then() + "for " + func_to_str(func) + "(" + str(n) +")" )

##then = timestamp()
##n = 40
##print (Fibonacci.fib_iteration(n))
##print ("%1.8f seconds " %then() + "for fib_iteration(" + str(n) +")" )
    
functions = [[Fibonacci.fib_iteration, 40],
             [Fibonacci.fib_recursion, 20],
             [Fibonacci.fib_recursion18, 20]
             ]
for each_func in functions:
    run_fibonacci_func(each_func[0], each_func[1])

then = timestamp()
n = 40
print (Fibonacci.fib_lookuptable(n, {1:1, 2:1}))
print ("%1.8f seconds " %then() + "for fib_lookuptable(" + str(n) +")" )           
                       

