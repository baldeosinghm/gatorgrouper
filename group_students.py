""" Group the student identifiers """

from random import shuffle
import argparse
import itertools
import sys
import logging
#default values
from defaults import *

def group_students(student_identifers, group_size):
    iterable = iter(student_identifers)
    # use itertools to chunk the students into groups
    student_groups = list(
        iter(lambda: list(itertools.islice(iterable, group_size)), []))
    # merge a single student into the previous group
    last_group_index = len(student_groups) - 1
    if len(student_groups[last_group_index]) == SINGLETON_GROUP:
        logging.info("Removing last group with only one member and placing member into previous group.")
        receiving_group = student_groups[last_group_index - 1]
        too_small_group = student_groups[last_group_index]
        receiving_group.append(*too_small_group)
        student_groups.remove(too_small_group)
    return student_groups
