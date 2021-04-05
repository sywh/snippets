
class Greeter(object):
    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable

    # Instance method
    def hello(name, loud=False):  # loud is optional
        if loud:
            print('HELLO, %s' % name.upper())
        else:
            print('Hello, %s!' % name)

g = Greeter('Fred')
g.greet()
g.greet(loud=True)