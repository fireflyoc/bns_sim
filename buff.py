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
    def __init__(self, duration=0, damage=0, tick=1, name=""):
        self.max_duration = duration
        self.remaining = duration
        self.damage = damage
        self.tick_interval = tick
        self.name = name
        
        
        
overflow = Buff(duration=5, name="Overflow")
photosynthesis = Buff(duration = 5, name = "Photosynthesis")    
magnum = Buff(duration = 10,name = "Magnum")
magnum_final = Buff(duration = 15, name = "magnum 3 stacks")
burr_available = Buff(duration = 30, name = "Burr Toss Available")
bracelet = Buff(duration = 10, name = "Divinity Bracelet")
dynasty = Buff(stacks = 3, duration = 4, name = "Dynasty Mystic Badge")
ssf_available = Buff(duration = 5, name = "Super Sunflower Available")

poison = Debuff(duration = 10, damage = 0.6, tick = 1, name = "Ivy Poison")