# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 13:30:53 2019

@author: Noah G
"""

class Player:
    def __init__(self, att_pwr = 0, ele = 1, c_rate = 0, c_dmg = 1, skill_list = []):
        self.attack_power = att_pwr
        self.elemental = ele
        self.crit_rate = c_rate
        self.crit_damage = c_dmg
        self.max_focus = 10
        self.current_focus=10
        self.buffs = []
        self.skills = skill_list
        
        
    def get_stats(self):
        ap, ele, crit, cdmg = self.attack_power, self.elemental, self.crit_rate, self.crit_damage
        for buf in self.buffs:
            ap += (buf.ap_buff * buf.stacks)
            crit += (buf.crit_buff * buf.stacks)
            cdmg += (buf.crit_dmg_buff * buf.stacks)
            ele += (buf.elemental_buff * buf.stacks)
            
        return ap, ele, crit, cdmg

class Target:
    def __init__(self):
        self.debuffs = []