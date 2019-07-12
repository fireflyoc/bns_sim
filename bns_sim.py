# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:57:45 2018

@author: Noah G
"""

import random
from soul import soul
from buff import *
from skill import *
from gcd_object import gcd_object
from apl_item import apl_item
from actors import Player, Target
from sim_result import SimResult
import time



total_dmg = 0
sim_list = []
target = Target()

def run_sim(time = 300):
    global total_dmg, sim_list
    
    total_dmg = 0
    clock = 0
    clock_tick = 0.1
    
    gcd1a = gcd1
    gcd2a = gcd2
    gcd3a = gcd3

    
    char = Player(att_pwr = 1171, ele = 1.4464, c_rate = 0.5523, c_dmg = 2.5, skill_list = [rosethorn, sunflower, super_sunflower, 
                                                                               thorn_strike, petal_storm, burr_toss,
                                                                               grasping_roots, flying_nettles])
    
    cosmic = soul()
    soul_buff = Buff(ap = cosmic.ap, c_rate = cosmic.crit_buff, c_dmg = cosmic.crit_dmg_buff, duration = 5, name = "soul")
    
    while clock < time:
    
        apl = []
        apl.append(apl_item(skill=flying_nettles, conditions=[clock<5]))
        apl.append(apl_item(skill=grasping_roots, conditions=[all([True if not poison.name == db.name else False for db in target.debuffs])]))
        apl.append(apl_item(skill=thorn_strike))
        apl.append(apl_item(skill=flying_nettles, conditions=[any([True if magnum_final.name == buff.name else False for buff in char.buffs])]))
        apl.append(apl_item(skill=burr_toss, conditions=[any([True if burr_available.name == buff.name else False for buff in char.buffs])]))
        apl.append(apl_item(skill=petal_storm, conditions=[all([True if not buff.name == bracelet.name else False for buff in char.buffs])]))
        apl.append(apl_item(skill=super_sunflower))
        apl.append(apl_item(skill=sunflower))
        apl.append(apl_item(skill=rosethorn))
        
        #this is where the APL comes in
        if cosmic.remaining_cooldown <=0:
            soul_buff.duration = cosmic.duration
            char.buffs.append(soul_buff)
            cosmic.remaining_cooldown = cosmic.cooldown
            cosmic.remaining_duration = cosmic.duration
#            print(clock, "add soul buff")
        
        for i, item in enumerate(apl):
            if item.can_use(item.skill.can_use(char,target)):
                print(round(clock,2), i, item.skill.name, char.current_focus, sep=' | ')
                total_dmg += item.skill.cast(char, target)
                print([(buff.name, buff.stacks) for buff in char.buffs])
                print([(db.name, round(db.remaining,2)) for db in target.debuffs])
                print([(sk.name, round(sk.remaining_cd,2)) for sk in char.skills])
                print("---------------")
                break
   
        clock+=clock_tick
        
        for ability in char.skills:
            ability.remaining_cd -= clock_tick
            
        cosmic.remaining_cooldown -= clock_tick
        cosmic.remaining_duration -= clock_tick
        for buf in char.buffs:
            buf.duration -= clock_tick
            if buf.duration <= 0 or buf.stacks <= 0:
                char.buffs.remove(buf)
#                print(clock, "remove buff: ", buf.name)
        for debuff in target.debuffs:
            debuff.remaining -= clock_tick
            if debuff.remaining % debuff.tick_interval == 0:
                total_dmg += char.attack_power * char.elemental * debuff.damage
            if debuff.remaining <= 0:
                target.debuffs.remove(debuff)
                
        gcd1a.wait_time -= clock_tick
        gcd2a.wait_time -= clock_tick
        gcd3a.wait_time -= clock_tick
        
                
#    sim_list.append(total_dmg/clock)
    sim_list.append(SimResult(damage = total_dmg, time = clock, skills = char.skills))
    
start = time.time()
for i in range(1):
    run_sim(random.uniform(27, 33))
    
print("Finish: %d seconds" % int(time.time() - start))

temp_dmg = 0
temp_time = 0
skill_counts = [[sk.name, 0] for sk in sim_list[-1].skills]
skill_crits = [[sk.name, 0] for sk in sim_list[-1].skills]
for run in sim_list:
    temp_dmg += (run.damage/run.length)
    temp_time += run.length
    for i, sk in enumerate(run.skills):
        skill_counts[i][1] += sk.total_uses
        skill_crits[i][1] += sk.total_crits

print("Average:\t", temp_dmg/len(sim_list))
print("Max:\t\t", max([run.damage/run.length for run in sim_list]))
print("Min:\t\t", min([run.damage/run.length for run in sim_list]))
print("Average Time: \t", temp_time/len(sim_list))
print("-----------------------")
for i, sk in enumerate(skill_counts):
    print(skill_counts[i][0], "Uses:", skill_counts[i][1]/len(sim_list), "\tCrits:", skill_crits[i][1]/len(sim_list))


