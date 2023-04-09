s = "hello"


def reverse_slicing(s):
    """_summary_

    Args:
        s (_type_): str

    Returns:
        _type_: list
    """
    result = s[::-1]
    return result


def reverse_list(s):
    """_summary_

    Args:
        s (_type_): str

    Returns:
        _type_: str
    """
    temp_list = list(s)
    temp_list.reverse()
    result = ''.join(temp_list)
    return result


def reverse_join_reversed_iter(s):
    """_summary_

    Args:
        s (_type_): str

    Returns:
        _type_: str
    """
    s1 = ''.join(reversed(s))
    return s1


def reverse_for_loop(s):
    """_summary_

    Args:
        s (_type_): str

    Returns:
        _type_: str
    """
    result = ""
    for c in s:
        # appending chars in reverse order
        result = c + result

    return result


print(reverse_s)
print(reverse_list(s))
print(reverse_join_reversed_iter(s))
print(reverse_for_loop(s))
