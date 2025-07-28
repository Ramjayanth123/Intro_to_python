while True:
    try:

        age = int(input('Enter your age (1-120):'))

        if age<1 or age>120:
            print('Please enter a valid number in the given range')
            continue
        print('You have entered a valid input{}'.format(age))
        break
    except ValueError:
        print('You have entered an invalid number')

    



    