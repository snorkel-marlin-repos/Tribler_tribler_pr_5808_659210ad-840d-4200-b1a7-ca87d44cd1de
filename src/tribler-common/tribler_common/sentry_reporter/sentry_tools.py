""" This a collection of tools for SentryReporter and SentryScrubber aimed to
simplify work with several data structures.
"""


def parse_os_environ(array):
    """ Parse os.environ field.

    Args:
        array: strings that represents tuples delimited by `:`
            Example: ["KEY:VALUE", "PATH:~/"]

    Returns:
        Dictionary that made from given array.
            Example: {"KEY": "VALUE", "PATH": "~/"}

    """
    result = {}

    if not array:
        return result

    for line in array:
        items = line.split(':', 1)
        if len(items) < 2:
            continue
        result[items[0]] = items[1]

    return result


def parse_stacktrace(stacktrace):
    """ Parse stacktrace field.

    Args:
        stacktrace: a string with '\n' delimiter.
            Example: "line1\nline2"

    Returns:
        The list of strings made from the given string.
            Example: ["line1", "line2"]
    """
    if not stacktrace:
        return []

    return [line for line in stacktrace.split('\n') if line]


def get_first_item(items, default=None):
    return items[0] if items else default


def get_last_item(items, default=None):
    return items[-1] if items else default


def delete_item(d, key):
    if not d:
        return d

    if key in d:
        del d[key]
    return d


def get_value(d, key, default=None):
    return d.get(key, default) if d else default


def modify_value(d, key, function):
    if not d or not key or not function:
        return d

    if key in d:
        d[key] = function(d[key])

    return d
