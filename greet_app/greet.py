def greet(name):
    if isinstance(name, str):
        if name.isupper():
            return f"HELLO {name}!"
    elif isinstance(name, (list, tuple)):
        return f"Hello, {' and '.join(name) if len(name) == 2 else ''}."
    elif name is None:
        name = "my friend"
    return f"Hello, {name}."
