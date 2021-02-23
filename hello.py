# variables don't need to be declared beforehand
# declaring a variable like below creates an object with an id number - the declared variable is just a name that knows to point to that object id number
# because of this, declared variables with the same value actually reference the same object
# strings can also be multiplied (? weird)
msg1 = "Hello World!"
msg2 = "Hello World!"
print(msg1)
print(id(msg1), id(msg2))

# we can use the % operator to format a set of variables enclosed in a tuple together with a format string
# tuples are fixed size lists
# format strings contain normal text together with 'argument specifiers' like %s or %d
name = "John"
age = 23
print("%s is %d years old." % (name, age))
# any object which is not a string can be formatted using the %s operator as well. The string which returns from the "repr" method of that object is formatted as the string
mylist = [1, 2, 3]
print("A list: %s" % mylist)
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)
# seems like the % operator moves from 'index' 1 to 2 to the next when there are multiple instances of the same % in a format string, see below
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)


# lists are array-like objects
# they can be added together or multiplied like strings above
# they can be looped over with a number of different methods
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
# break and continue are ways to interact more robustly with these loop methods
count = 0
while True:
    print(count)
    count += 1
    if count >= 3:
        break
for x in range(6):
    if x % 2 == 0:
        continue
    print(x)

# functions use the block keyword def and are pretty similar to how they work in other languages I've worked with


def greet(name):
    """
    docstring explaining function purpose goes here
    for example, this one takes a name and prints a string including that name to console
    """
    print("Hello there", name)
