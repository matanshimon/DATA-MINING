def my_func(x1,x2,x3):
    if not all(isinstance(x,float) for x in [x1,x2,x3]):
        print("“Error: parameters should be float”")
        return None
    my_sum = x1+x2+x3
    if my_sum == 0:
        print("Not a number – denominator equals zero")
        return None
    else:
        my_result = (my_sum * (x2 + x3) * x3) / my_sum
        return float(my_result)
print(my_func(4.0,8.0,-6.0))
