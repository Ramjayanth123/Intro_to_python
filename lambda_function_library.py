factorial = lambda n : 1 if n == 0 else n * factorial(n-1)
square = lambda x : x**2 
reverse = lambda s: s[::-1]
upper = lambda s : s.upper()

filter_even = lambda lst : list(filter(lambda x : x%2==0,lst))
sum_list = lambda lst : sum(lst)
l = [1,2,3,4,5,6,7,8,9]
print(filter_even([2,6,5,4,8,7]))
print(square(6))
print(upper("ramjayanth"))
print(reverse('htnayajmar'))
print(sum_list(l))