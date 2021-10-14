"""Determine whether the Human Readable Boolean functions properly."""

# Reference:
# https://docs.pytest.org/en/6.2.x/
from palindromechecker import util


def test_human_readable_boolean_true():
    """Ensure that a human-readable true boolean works correctly."""
    true_value = True
    true_value_human_readable = util.get_human_readable_boolean(true_value)
    assert true_value_human_readable == "Yes, it is!"


def test_human_readable_boolean_false():
    """Ensure that a human-readable false boolean works correctly."""
    false_value = False
    false_value_human_readable = util.get_human_readable_boolean(false_value)
    assert false_value_human_readable == "No, it is not!"
