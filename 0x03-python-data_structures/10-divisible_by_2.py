#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list.
    Parameters
        ----------
        filename: my_list
        Returns
        ----------
        String
     """
    multiples = []
    for j in range(len(my_list)):
        if my_list[j] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)
    return (multiples)
