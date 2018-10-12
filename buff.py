# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 23:01:30 2018

@author: Noah G
"""

class buff:
    def __init__(self, ap = 0, c_rate=0, c_dmg=0, stacks=1, ele = 0, duration = 0, name = ""):
        self.ap_buff = ap
        self.crit_buff = c_rate
        self.crit_dmg_buff = c_dmg
        self.stacks = stacks
        self.elemental_buff = 0
        self.duration = duration
        self.name = name