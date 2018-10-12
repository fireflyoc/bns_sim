# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:57:45 2018

@author: AF95026
"""

import random
from soul import soul
from buff import buff
from skill import skill
from gcd_object import gcd_object

class player:
    def __init__(self, att_pwr = 0, ele = 1, c_rate = 0, c_dmg = 1):
        self.attack_power = att_pwr
        self.elemental = ele
        self.crit_rate = c_rate
        self.crit_damage = c_dmg
        self.max_focus = 10
        self.current_focus=10
        self.buffs = []

char = player(1171, 1.4464, 0.5523, 2.5)
total_dmg = 0
sim_list = []

rosethorn = skill("rosethorn", 1.7, 0.4, -1, 0.4)
sunflower = skill("sunflower", 7.6, 0.5, 3, 0.5)
#    super_sunflower = skill("super sunflower", 9.6, 0.5, 2, 0.5)
thorn_strike = skill("thorn strike", 5.5, 1, 2, 18)
Doom_bloom = skill("doom and bloom", 6.4, 1, 0, 18)
flying_nettles = skill("flying nettles", 12.5, 1, 0, 18)
weed_whack = skill("weed whack", 7.5, 0.5, 2, 24)
petal_storm = skill("petal storm toss", 20, 1, 2, 24)

cosmic = soul()
soul_buff = buff(cosmic.ap, cosmic.crit_buff, cosmic.crit_dmg_buff, 1, 0, 5)

gcd1 = gcd_object()
gcd1.skill_list.append(rosethorn)
gcd2 = gcd_object()
gcd2.skill_list.append(sunflower)
gcd3 = gcd_object()
gcd3.skill_list.append(thorn_strike)
gcd3.skill_list.append(Doom_bloom)
gcd3.skill_list.append(weed_whack)
gcd3.skill_list.append(petal_storm)
gcd3.skill_list.append(flying_nettles)

def attack(ability):
    global total_dmg
#    calculate damage
    ap = char.attack_power
    crit = char.crit_rate
    cdmg = char.crit_damage
    ele = char.elemental
#    for buf in char.buffs:
#        ap += buf.ap_buff
#        crit += buf.crit_buff
#        cdmg += buf.crit_dmg_buff
#        ele += buf.elemental_buff
        
    skill_dmg = random.uniform(ability.ap_modifier*0.9, ability.ap_modifier*1.1)*ap*ele
    if random.random() < crit:
        skill_dmg *= cdmg
        ability.total_crits += 1
    total_dmg += skill_dmg
#    put the skill on cd
    ability.remaining_cd = ability.cooldown
    ability.total_uses += 1
    ability.total_dmg += skill_dmg
    
    char.current_focus -= ability.focus_cost
    if char.current_focus > char.max_focus:
        char.current_focus = char.max_focus


#for i in range(0,500):
#    attack(rosethorn)
    
def run_sim(time = 300):
    global total_dmg, sim_list
    
    total_dmg = 0
    clock = 0
    clock_tick = 0.1
    while clock < time:
        #this is where the APL comes in
#        if cosmic.remaining_cooldown <=0:
#            char.buffs.append(soul_buff)
#            cosmic.remaining_cooldown = cosmic.cooldown
#            cosmic.remaining_duration = cosmic.duration
        
        for ability in gcd3.skill_list:
            if ability.remaining_cd <= 0 and char.current_focus >= ability.focus_cost:
                attack(ability)
                break
        else:
            for ability in gcd1.skill_list:
                if ability.remaining_cd <= 0 and char.current_focus >= ability.focus_cost:
                    attack(ability)
                    break
            else:
                for ability in gcd2.skill_list:
                    if ability.remaining_cd <=0 and char.current_focus >= ability.focus_cost:
                        attack(ability)
                        break
        
        clock+=clock_tick
        for ability in gcd1.skill_list:
            ability.remaining_cd -= clock_tick
        for ability in gcd2.skill_list:
            ability.remaining_cd -= clock_tick
        for ability in gcd3.skill_list:
            ability.remaining_cd -= clock_tick
#        cosmic.remaining_cooldown -= clock_tick
#        cosmic.remaining_duration -= clock_tick
#        for buf in list(char.buffs):
#            buf.duration -= clock_tick
#            if buf.duration <= 0:
#                char.buffs.remove(buf)
                
    sim_list.append(total_dmg/clock)
    
for i in range(1):
    run_sim(random.uniform(270, 330))

temp = 0
for run in sim_list:
    temp += run

print(temp/len(sim_list))

