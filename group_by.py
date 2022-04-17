from collections.abc import Iterable
from typing import Optional


def group_by(function: Optional[callable], iterable: Iterable) -> dict:
    # return_dict = {}
    # for item in iterable:
    #     if function(item) in return_dict.keys():
    #         return_dict[function(item)].append(item)
    #     else:
    #         return_dict[function(item)] = item
    return {function(item): item for item in iterable}
    # return return_dict


if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))
