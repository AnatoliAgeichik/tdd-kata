def get_string_with_all_names(names):
    return f"{', '.join(names[:-1])}{' and ' if len(names) > 1 else ''}{names[-1]}"


def greet_with_many_names(names):
    return f"Hello, {get_string_with_all_names(names)}."


def greet_uppercase(names):
    return f"HELLO {get_string_with_all_names(names)}!"


def split_names(names: str) -> list:
    return [x.strip() for x in names.split(',')]


def handle_many_names(names):
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
        names_list = split_names(names)
        if names.isupper():
            return greet_uppercase(names_list)
        return handle_many_names(names_list)
    elif isinstance(names, (list, tuple)):
        names_list = []
        for name in names:
            if name[0] == '"':
                names_list.append(name)
            else:
                names_list += split_names(name)
        return handle_many_names(names_list)
    elif names is None:
        names = "my friend"
    return f"Hello, {names}."
