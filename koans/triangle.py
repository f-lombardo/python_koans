#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    sides = [a, b, c]

    check_if_valid(sides)

    nr_of_different_sides = len(set(sides))
    if nr_of_different_sides == 3:
        return 'scalene'
    elif nr_of_different_sides == 2:
        return 'isosceles'
    else:
        return 'equilateral'


def check_if_valid(sides):
    sum_all_sides = sum(sides)
    for side in sides:
        if side <= 0:
            raise TriangleError
        sum_others = sum_all_sides - side
        if side >= sum_others:
            raise TriangleError


# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
