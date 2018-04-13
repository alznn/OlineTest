def anonymous(x):
    return x**2+1
def intergate (fun,start,end):
    step = 0.1
    intercept = start
    area = 0
#    tmp = 0
    while intercept < end:
        intercept+=step
        #底乘高+前面面積
        area = fun(intercept)*step + area

    return area
print(intergate(anonymous,0,10))