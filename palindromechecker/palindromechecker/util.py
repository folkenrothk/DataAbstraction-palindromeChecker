"""Implement the utilities (reading booleans) needed for this program."""


def get_human_readable_boolean(boolean: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    # the provided answer is True
    if boolean is True:
        return "Yes, it is!"
    # the provided answer is False
    return "No, it is not!"
