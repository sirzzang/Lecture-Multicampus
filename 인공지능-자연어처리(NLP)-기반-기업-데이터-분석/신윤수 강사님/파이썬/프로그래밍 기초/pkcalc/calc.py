# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:22:33 2020

@author: student
"""

name = 'calc'

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

class CalcClass:
    def __init__(self, *args):
        self.values = args
        
    def get_result(self):
        print("sum: {0}, sub: {1}".format(sum(self.values), self.values[0] - sum(self.values[1:])))
    