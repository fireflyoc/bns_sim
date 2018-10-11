# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:57:45 2018

@author: AF95026
"""

import random

class player:
    def __init__(self, att_pwr = 0, ele = 1, c_rate = 0, c_dmg = 1):
        self.attack_power = att_pwr
        self.elemental = ele
        self.crit_rate = c_rate
        self.crit_damage = c_dmg
        self.max_focus = 10
        self.current_focus=10
        self.buffs = []
    
        
class skill:
    def __init__(self, ap_mod = 1, gcd_time = 1, focus_cost = 0, cd = 1):
        self.ap_modifier = ap_mod
        self.variance = 0.1
        self.gcd_timer = gcd_time
        self.total_uses = 0
        self.total_crits = 0
        self.focus_cost = focus_cost
        self.cooldown = cd
        self.remaining_cd = 0
        
class gcd_object:
    def __init__(self):
        self.wait_time = 0
        self.skill_list = []
        
        
        
char = player(1150, 1.45, 0.67, 2.48)
rosethorn = skill(1.5, 0.4, -1, 0.4)
sunflower = skill(4.5, 0.5, 3, 0.5)
super_sunflower = skill(6.5, 0.5, 2, 0.5)

gcd1 = gcd_object()
gcd1.skill_list.append(rosethorn)
gcd2 = gcd_object()
gcd2.skill_list.append(sunflower)


clock = 0
total_dmg = 0

def attack(skill):
    global total_dmg
#    calculate damage
    skill_dmg = random.uniform(skill.ap_modifier*0.9, skill.ap_modifier*1.1)*char.attack_power*char.elemental
    if random.random() < char.crit_rate:
        skill_dmg *= char.crit_damage
        skill.total_crits += 1
    total_dmg += skill_dmg
#    put the skill on cd
    skill.remaining_cd = skill.cooldown
    skill.total_uses += 1
    
    char.current_focus -= rosethorn.focus_cost
    if char.current_focus > char.max_focus:
        char.current_focus = char.max_focus


#for i in range(0,500):
#    attack(rosethorn)
clock_tick = 0.1
while clock < 300:
    #this is where the APL comes in
    for skill in gcd1.skill_list:
        if skill.remaining_cd <= 0:
            attack(skill)
            break
        
    for skill in gcd2.skill_list:
        if skill.remaining_cd <= 0:
            attack(skill)
            break
    
    
    clock+=clock_tick
    for skill in gcd1.skill_list:
        skill.remaining_cd -= clock_tick
    for skill in gcd2.skill_list:
        skill.remaining_cd -= clock_tick
    
print(total_dmg/300)

