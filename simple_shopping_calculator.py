p1=int(input('Enter the price of item1: '))
q1=int(input('Enter the quantity of item1: '))
p2=int(input('Enter the price of item2: '))
q2=int(input('Enter the quantity of item2: '))
p3=int(input('Enter the price of item3: '))
q3=int(input('Enter the quantity of item3: '))
total = (p1*q1) +(p2*q2) + (p3*q3)
tax = (total*0.085)
total_tax = total + tax

final_str= f'''
Item 1: {p1} x {q1} = {p1*q1}
Item 2: {p2} x {q2} = {p2*q2}
Item 3: {p3} x {q3} = {p3*q3}
Subtotal: {total}
Tax (8.5%): {tax}
Total: {total_tax}
'''

print(final_str)
