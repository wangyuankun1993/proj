# -*- coding:utf-8 -*-
# Product Name: PyCharm
# Project Name: proj
# File Name: test_progression.py
# Date: 2022/02/01 01:04:34
# Author: wangyuankun
# Function: This file is to achieve xxx function!
from progression import Progression
from arithmetic_progression import ArithmeticProgression
from geometric_progression import GeometricProgression
from fibonacci_progression import FibonacciProgression

if __name__ == '__main__':
    print('Default progression:')
    Progression().print_progression(10)

    print('Arithmetic progression with increment 5:')
    ArithmeticProgression(5).print_progression(10)

    print('Arithmetic progression with increment 5 and start 2:')
    ArithmeticProgression(5,2).print_progression(10)

    print('Geometric progression with default base:')
    GeometricProgression().print_progression(10)

    print('Geometric progression with base 3:')
    GeometricProgression(3).print_progression(10)

    print('Fibonacci progression with default start values:')
    FibonacciProgression().print_progression(10)
