print('Enter your name: ')
name = input()

print('Enter your age: ')
age = input()

print('Enter your location: ')
location = input()


message = "Hello {}, you are {} years old and live in {}.".format(name, age, location)

print(message)