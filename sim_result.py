# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:02:47 2019

@author: AF95026
"""

class SimResult:
    def __init__(self, damage=0, time = 0, skills = []):
        self.damage = damage
        self.skills = skills
        self.length = time
        