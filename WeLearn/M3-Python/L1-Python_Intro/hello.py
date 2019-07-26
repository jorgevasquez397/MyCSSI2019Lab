print("Hello py")
print("Bye py")
num1 = int(raw_input('Enter number #1'))
num2 = int(raw_input('Enter number #2'))
total = num1 + num2
print('The sum is ' + str(total))

num = int(raw_input("Enter a number: "))
if num > 0:
    print ("That's a positive number!")
elif num < 0:
    print("That's a negative number!")
else:
    print("Zero is neither positive nor negative")

string = 'hello there'
for letter in string:
    print(letter.upper())
for i in range(5):
    print(i)

my_name = "Bob"
friend1 = "Alice"
friend2 = "John"
friend3 = "Mallory"

print(
    "My name is %s and my friends are %s, %s, and %s" %
    (my_name, friend1, friend2, friend3)
)

def greetAgent(first_name, last_name):
    print("%s. %s %s." % (last_name, first_name, last_name))
greetAgent("Jorge", "Vasquez")
