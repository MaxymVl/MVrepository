def my_sum(*args, start=0):
    args_sum = sum(args)
    y = int(start)
    p = args_sum + y
    return p
print (my_sum(1,2,3,4,5,10, start=0 )) 
print (my_sum(1,2,3,4,5,155, ))
