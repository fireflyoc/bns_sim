# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:09:27 2019

@author: AF95026
"""

class apl_item:
    def __init__(self, skill, conditions=[]):
        self.skill = skill
        self.conditions = conditions
        
    def can_use(self):
        return all(self.conditions)
