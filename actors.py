# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:30:53 2019

@author: Noah G
"""

class Player:
    def __init__(self, att_pwr = 0, ele = 1, c_rate = 0, c_dmg = 1):
        self.attack_power = att_pwr
        self.elemental = ele
        self.crit_rate = c_rate
        self.crit_damage = c_dmg
        self.max_focus = 10
        self.current_focus=10
        self.buffs = []

class Target:
    def __init__(self):
        self.debuffs = []