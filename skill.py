# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 23:00:29 2018

@author: Noah G
"""

class skill:
    def __init__(self, name, ap_mod = 1, gcd_time = 1, focus_cost = 0, cd = 1):
        self.skill_name = name
        self.ap_modifier = ap_mod
        self.variance = 0.1
        self.gcd_timer = gcd_time
        self.total_uses = 0
        self.total_crits = 0
        self.focus_cost = focus_cost
        self.cooldown = cd
        self.remaining_cd = 0
        self.total_dmg = 0