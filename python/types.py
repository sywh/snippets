
# numbers: int, float
def numbers():
    x = 3
    print(type(x))  # Prints "<type 'int'>"
    print(x)
    print(x + 1)
    print(x - 1)
    print(x * 2)
    print(x ** 2)
    x += 1
    print(x)
    x *= 2
    print(x)
    y = 2.5
    print(type(y))  # Prints "<type 'float'>"
    print(y, y + 1, y * 2, y**2)
    # NOTE: there is no x++ or x-- in python


# boolean
def boolean():
    t = True
    f = False
    print(type(t))  # Prints "<type 'bool'>"
    print(t and f)
    print(t or f)
    print(not t)
    print(t != f)  # Logical XOR, prints "True"
    # NOTE: python use and, or, not, not &&, ||, !


# string
def string():
    hello = 'hello'
    world = "world"
    print(hello)
    print(len(hello))
    hw = hello + ' ' + world
    print(hw)
    hw12 = '%s %s %d' % (hello, world, 12)
    print(hw12)  # prints "hello world 12"

    s = "hello"
    print(s.capitalize())  # "Hello"
    print(s.upper())  # "HELLO"
    print(s.rjust(7))  # padding with spaces, prints "  hello"
    print(s.center(7))  # " hello "
    print(s.replace('l', '(ell)'))  # "he(ell)(ell)o"
    print('  world '.strip())  # strip leading and trailing whitespace, prints "world"