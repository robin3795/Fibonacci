
def fib_iteration(num): # simple iteration function
    if num < 3:
        return 1
    a = b = 1
    for i in range(2, num):
        a, b = b, a + b
    return b

def fib_recursion(num):    # recursion, too slow
    if num < 3:
        return 1
    return fib_recursion(num-1) + fib_recursion(num-2)

def fib_recursion18(num): # recursion with more initial values
    if num < 18:
        return [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597][num]#17 base cases
    return fib_recursion18(num-1) + fib_recursion18(num-2)

def fib_lookuptable(num, dict): # memoization :dynamic (changing) look-up table
    if num in dict:
       return dict[num]
    dict[num] = fib_lookuptable(num-1, dict) + fib_lookuptable(num-2, dict)
    return dict[num]

def fib_Dictionary(num): # global dictionary
    if num in fib_Dictionary.dict:
        return fib_Dictionary.dict[num]
    fib_Dictionary.dict[num] = fib_Dictionary(num-1) + fib_Dictionary(num-2)
    return fib_Dictionary.dict[num]
fib_Dictionary.dict = {1:1, 2:1}


