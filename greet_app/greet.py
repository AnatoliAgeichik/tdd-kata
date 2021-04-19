def greet(name):
    if name is None:
        name = "my friend"
    if name.isupper():
        return "HELLO {}!".format(name)
    return "Hello, {}.".format(name)
