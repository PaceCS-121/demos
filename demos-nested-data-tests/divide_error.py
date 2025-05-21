# math
# a = float(input('Enter numerator: '))
# b = float(input('Enter denominator: '))

# try:
#     answer = a / b
# except ZeroDivisionError:
#     print('no dividing by 0!')

# # this wasn't declared if the user tried to divide by 0!
# print(answer) 




test_types = {
    'simple': 'common',
    'edge': 'weird situation',
    'corner': 'really weird situation'
}

try:
    key = input('What type of test do you want to know about?')
    print(test_types[key])
except KeyError:
    print("Sorry can't find that one")
except KeyboardInterrupt:
    print('\nBye then')