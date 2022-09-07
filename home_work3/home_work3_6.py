from re import S


def my_sum(*args, start):
    args_sum = sum(args)
    y = int(start)
    p = args_sum + y
    return p
print (my_sum(1,2,3,4,5,10, start = 10)) 
print (my_sum(1,2,3,4,5,155, start = 0))