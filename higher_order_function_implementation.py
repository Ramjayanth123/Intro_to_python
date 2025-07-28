def custom_map(fun, iterable):
    return [fun(item) for item in iterable]

def custom_filter(fun, iterable):
    return [x for x in iterable if fun(x)]

def custome_reduce(fun, iterable):
    result = iterable[0]
    for x in iterable[1:]:
        result = fun(result, x)
    return result

print(custom_map(lambda x : x*2,[1,2,3]) )
print(custom_filter(lambda x : x%2==0,[1,2,3,4]))
print(custome_reduce(lambda x,y : x+y,[1,2,3,4]))







