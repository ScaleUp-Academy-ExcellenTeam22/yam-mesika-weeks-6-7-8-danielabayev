from collections.abc import Iterable
from typing import Optional


def group_by(function: Optional[callable], iterable: Iterable) -> dict:
    """
    This function receive function and iterable and return dictionary where the keys are the results of the function and
     the values are the values in the iterables.
    :param function: Function to apply.
    :param iterable: Items to run the function on.
    :return: Dictionary base on the results of the function and the iterable.
    """
    return_dict = {}
    for item in iterable:
        if function(item) in return_dict.keys():
            return_dict[function(item)].extend([item])
        else:
            return_dict[function(item)] = [item]
    return return_dict


if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))
