def greet_with_many_names(names):
    return f"Hello, {', '.join(names[:-1])}{' and ' if len(names) > 1 else ''}{names[-1]}."


def greet_uppercase(names):
    return f"HELLO {', '.join(names[:-1])}{' and ' if len(names) > 1 else ''}{names[-1]}!"


def split_names(names: str) -> list:
    return list(map(lambda x: x.strip(), names.split(',')))


def handler_many_names(names):
    names_uppercase = []
    filtered_names = []

    for name in names:
        if name.isupper():
            names_uppercase.append(name.strip('"'))
        else:
            filtered_names.append(name.strip('"'))
    return f"{greet_with_many_names(filtered_names) if len(filtered_names) > 0 else ''}" \
           f"{f' AND {greet_uppercase(names_uppercase)}' if len(names_uppercase) > 0 else ''}"


def greet(names):
    if isinstance(names, str):
        list_names = split_names(names)
        if names.isupper():
            return greet_uppercase(list_names)
        return handler_many_names(list_names)
    elif isinstance(names, (list, tuple)):
        list_names = []
        for name in names:
            if name[0] == '"':
                list_names.append(name)
            else:
                list_names += split_names(name)
        return handler_many_names(list_names)
    elif names is None:
        names = "my friend"
    return f"Hello, {names}."
