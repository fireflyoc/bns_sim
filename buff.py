# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 23:01:30 2018

@author: Noah G
"""

class Buff:
    def __init__(self, ap = 0, c_rate=0, c_dmg=0, stacks=1, ele = 0, duration = 0, name = "", other = None):
        if other:
            self.ap_buff = other.ap_buff
            self.crit_buff = other.crit_buff
            self.crit_dmg_buff = other.crit_dmg_buff
            self.stacks = other.stacks
            self.elemental_buff = other.elemental_buff
            self.max_duration = other.duration
            self.duration = other.duration
            self.name = other.name
        else:
            self.ap_buff = ap
            self.crit_buff = c_rate
            self.crit_dmg_buff = c_dmg
            self.stacks = stacks
            self.elemental_buff = ele
            self.max_duration = duration
            self.duration = duration
            self.name = name
        
        
class Debuff:
    def __init__(self, duration, damage, tick, name):
        self.max_duration = duration
        self.remaining = duration
        self.damage = damage
        self.tick_interval = tick
        self.name = name