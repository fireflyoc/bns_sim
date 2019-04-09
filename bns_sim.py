# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:57:45 2018

@author: Noah G
"""

import random
from soul import soul
from buff import Buff, Debuff
from skill import ThornStrike,Sunflower,SuperSunflower,Rosethorn,FlyingNettles,BurrToss,GraspingRoots, PetalStormToss
from gcd_object import gcd_object
from apl_item import apl_item
from actors import Player, Target


char = Player(1171, 1.4464, 0.5523, 2.5)
total_dmg = 0
sim_list = []
target = Target()


def attack(ability, clock):
    global total_dmg, char
#    calculate damage
    ap = char.attack_power
    crit = char.crit_rate
    cdmg = char.crit_damage
    ele = char.elemental
    for buf in char.buffs:
        ap += (buf.ap_buff * buf.stacks)
        crit += (buf.crit_buff * buf.stacks)
        cdmg += (buf.crit_dmg_buff * buf.stacks)
        ele += (buf.elemental_buff * buf.stacks)
        
#    print(clock, ap)
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


    
def run_sim(time = 300):
    global total_dmg, sim_list
    
    gcd1 = gcd_object()
    gcd2 = gcd_object()
    gcd3 = gcd_object()

    rosethorn = Rosethorn(1.7, 0.4, -1, 0.4, gcd1)
    sunflower = Sunflower(4.8, 0.5, 3, 0.5, gcd2)
    super_sunflower = SuperSunflower(9.6, 0.5, 2, 0.5, gcd2)
    thorn_strike = ThornStrike(5.5, 1, 2, 18, gcd3)
#    Doom_bloom = skill("doom and bloom", 6.4, 1, 0, 18)
    flying_nettles = FlyingNettles(12.5, 1, 0, 18, gcd3)
    grasping_roots = GraspingRoots(7.5, 0.5, 2, 24, gcd3)
    petal_storm = PetalStormToss(20, 1, 2, 24, gcd3)
    burr_toss = BurrToss(37.5, 1, 0, 0, gcd3)
    
    poison = Debuff(10,0.6,1, "Ivy Poison")
    
    cosmic = soul()
    soul_buff = Buff(ap = cosmic.ap, c_rate = cosmic.crit_buff, c_dmg = cosmic.crit_dmg_buff, duration = 5, name = "soul")
    overflow = Buff(duration=5, name="overflow")
    photosynthesis = Buff(duration = 5, name = "Photosynthesis")    
    magnum = Buff(duration = 10,name = "Magnum")
    magnum_final = Buff(duration = 15, name = "magnum 3 stacks")
    burr_available = Buff(duration = 30, name = "Burr Toss Available")
    bracelet = Buff(duration = 10, name = "Divinity Bracelet")
    dynasty = Buff(stacks = 3, duration = 4, name = "Dynasty Mystic Badge")
    ssf_available = Buff(duration = 5, name = "Super Sunflower Available")
    
    apl = []
    apl.append(apl_item(thorn_strike,[thorn_strike.can_use(char)]))
    apl.append(apl_item(flying_nettles,[flying_nettles.can_use(char),magnum_final in char.buffs, poison in target.debuffs]))
    apl.append(apl_item(burr_toss,[burr_toss.can_use(char),burr_available in char.buffs]))
    apl.append(apl_item(petal_storm, [petal_storm.can_use(char), bracelet not in char.buffs]))
    apl.append(apl_item(grasping_roots, [grasping_roots.can_use(char), poison not in target.debuffs]))
    apl.append(apl_item(super_sunflower, [super_sunflower.can_use(char), (overflow in char.buffs or ssf_available in char.buffs)]))
    apl.append(apl_item(sunflower, [sunflower.can_use(char)]))
    apl.append(apl_item(rosethorn, [rosethorn.can_use(char)]))
    total_dmg = 0
    clock = 0
    clock_tick = 0.1
    while clock < time:
        #this is where the APL comes in
        if cosmic.remaining_cooldown <=0:
            soul_buff.duration = cosmic.duration
            char.buffs.append(soul_buff)
            cosmic.remaining_cooldown = cosmic.cooldown
            cosmic.remaining_duration = cosmic.duration
#            print(clock, "add soul buff")
        
        for item in apl:
            if item.can_use:
                total_dmg += item.skill.cast(char, target)
                break
        
        
        
#        for ability in gcd3.skill_list:
#            if gcd3.wait_time <=0 and ability.remaining_cd <= 0 and char.current_focus >= ability.focus_cost:
#                attack(ability, clock)
##                print(clock, ability.skill_name)
#                gcd3.wait_time = ability.gcd_timer
#                break
#        else:
#            for ability in gcd1.skill_list:
#                if gcd2.wait_time <=0 and ability.remaining_cd <= 0 and char.current_focus >= ability.focus_cost:
#                    attack(ability, clock)
#                    gcd2.wait_time = ability.gcd_timer
#                    break
#            else:
#                for ability in gcd2.skill_list:
#                    if gcd1.wait_time <=0 and ability.remaining_cd <=0 and char.current_focus >= ability.focus_cost:
#                        attack(ability, clock)
#                        gcd1.wait_time = ability.gcd_timer
#                        break
#        
        clock+=clock_tick
        for ability in gcd1.skill_list:
            ability.remaining_cd -= clock_tick
        for ability in gcd2.skill_list:
            ability.remaining_cd -= clock_tick
        for ability in gcd3.skill_list:
            ability.remaining_cd -= clock_tick
        cosmic.remaining_cooldown -= clock_tick
        cosmic.remaining_duration -= clock_tick
        for buf in char.buffs:
            buf.duration -= clock_tick
            if buf.duration <= 0 or buf.stacks <= 0:
                char.buffs.remove(buf)
#                print(clock, "remove buff: ", buf.name)
        for debuff in target.debuffs:
            debuff.duration -= clock_tick
            if debuff.duration % debuff.tick_interval == 0:
                total_dmg += char.attack_power * char.elemental * debuff.damage
            if debuff.duration <= 0:
                target.debuffs.remove(debuff)
                
        gcd1.wait_time -= clock_tick
        gcd2.wait_time -= clock_tick
        gcd3.wait_time -= clock_tick
        
                
    sim_list.append(total_dmg/clock)
    
for i in range(1000):
    run_sim(random.uniform(270, 330))

temp = 0
for run in sim_list:
    temp += run

print("Average: ", temp/len(sim_list))
print("Max: ", max(sim_list))
print("Min: ", min(sim_list))

