# This file contain the functions for scenario 2 and scenario 3


def scenario2(k, kbase=3.0, nabase=149.0):
    clbase = kbase + nabase
    init_c = {'K': [kbase, kbase + k],
              'Na': [nabase, nabase - 0.5 * k],
              'Cl': [clbase, clbase + 0.5 * k]}
    return init_c


def scenario3(k, kbase=3.0, nabase=149.0):
    clbase = kbase + nabase
    init_c = {'K': [kbase, kbase + k],
              'Na': [nabase, nabase],
              'Cl': [clbase, clbase + k]}
    return init_c
