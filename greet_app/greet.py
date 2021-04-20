def greet_with_many_names(names):
    return f"Hello, {', '.join(names[:-1])} and {names[-1]}."


def greet_uppercase(names):
    return f"HELLO {', '.join(names[:-1])}{' and ' if len(names) > 1 else ''}{names[-1]}!"


def greet(names):
    if isinstance(names, str):
        if names.isupper():
            return f"HELLO {names}!"
    elif isinstance(names, (list, tuple)):
        names_uppercase = []
        filtered_names = []
        for name in names:
            if name.isupper():
                names_uppercase.append(name)
            else:
                filtered_names.append(name)
        return f"{greet_with_many_names(filtered_names)}" \
               f"{f' AND {greet_uppercase(names_uppercase)}' if len(names_uppercase) > 0 else ''}"
    elif names is None:
        names = "my friend"
    return f"Hello, {names}."
