"""Implement a function that take a list and return a string joining list components with ', ' except the two last components that will be joined with ' and '.
"""


def comma_code(components):
    if len(components) > 2:
        comma_joined_components = ", ".join([str(c) for c in components[:-1]])
        last_component = components[-1]
        components = [comma_joined_components, last_component]

    return " and ".join([str(c) for c in components])


if __name__ == "__main__":
    pass
