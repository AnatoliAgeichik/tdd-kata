def greet(name):
    if name is None:
        name = "my friend"
    if isinstance(name, str):
        if name.isupper():
            return "HELLO {}!".format(name)
    else:
        if len(name) == 2:
            return "Hello, " + " and ".join(name) + "."
    return "Hello, {}.".format(name)
