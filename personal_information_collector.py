name = input('Enter your name: ')
age = int(input('Enter your age: '))
place= input('Enter your city: ')
hobby = input('Enter your hobby: ')
final_str = f'''
    Hello, {name}!
    You are {age} years old and live in {place}.
    In your free time, you enjoy {hobby}
    '''
print(final_str)