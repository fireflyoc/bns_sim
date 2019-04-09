# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 23:00:29 2018

@author: Noah G
"""
import random

class skill:
    variance = 0.1
    def __init__(self, ap_mod = 1, gcd_time = 1, focus_cost = 0, cd = 1, gcd):
        self.ap_modifier = ap_mod
        self.gcd_timer = gcd_time
        self.total_uses = 0
        self.total_crits = 0
        self.focus_cost = focus_cost
        self.cooldown = cd
        self.remaining_cd = 0
        self.total_dmg = 0
        self.gcd_obj = gcd
        
    def can_use(self,char):
        return all([self.focus_cost <= char.current_focus, self.gcd_obj.wait<=0, self.remaining_cd <=0])
    
    
class ThornStrike(skill): 
    def __init__(self):
        self.name = "Thorn Strike"
        
    def cast(self, char, target):
#        TODO: Implement
        ap = char.attack_power
        crit = char.crit_rate
        cdmg = char.crit_damage
        ele = char.elemental
        ap_mod = self.ap_modifier
        self.remaining_cd = self.cooldown
        for buf in char.buffs:
            ap += (buf.ap_buff * buf.stacks)
            crit += (buf.crit_buff * buf.stacks)
            cdmg += (buf.crit_dmg_buff * buf.stacks)
            ele += (buf.elemental_buff * buf.stacks)
            if buf.name== dynasty.name:
                ap_mod += 8
                self.remaining_cd = 0
                buf.stacks -= 1
            
        for debuff in target.debuffs:
            if debuff.name == poison.name:
                ap_mod +=6.5
                debuff.duration += 6
                if debuff.duration > debuff.max_duration:
                    debuff.duration = debuff.max_duration
        

        
        skill_dmg = random.uniform(ap_mod*(1-variance), ap_mod*(1+variance))*ap*ele
        if random.random() < crit:
            skill_dmg *= cdmg
            self.total_crits += 1
    #    put the skill on cd
        self.total_uses += 1
        self.total_dmg += skill_dmg
        
        char.current_focus -= self.focus_cost
        if char.current_focus > char.max_focus:
            char.current_focus = char.max_focus

        for buff in char.buffs:
            if buff.name == magnum.name:
                buff.stacks += 1
                if buff.stacks == 3:
                    char.buffs.remove(buff)
                    char.buffs.append(Buff(other=magnum_final))
        
        return skill_dmg
    
class Sunflower(skill):
    def __init__(self):
        self.name = "Sunflower"
    
    def cast(self, char, target):
        ap = char.attack_power
        crit = char.crit_rate
        cdmg = char.crit_damage
        ele = char.elemental
        ap_mod = self.ap_modifier
        
        for db in target.debuffs:
            if db.name == poison.name:
                ap_mod += 1
                char.buffs.append(Buff(ssf_available))
                
        for buf in char.buffs:
            ap += (buf.ap_buff * buf.stacks)
            crit += (buf.crit_buff * buf.stacks)
            cdmg += (buf.crit_dmg_buff * buf.stacks)
            ele += (buf.elemental_buff * buf.stacks)
            if buf.name == bracelet.name:
                ap_mod += 3.3
            
    #    print(clock, ap)
        skill_dmg = random.uniform(ap_mod*(1-variance), ap_mod*(1+variance))*ap*ele
        if random.random() < crit:
            skill_dmg *= cdmg
            self.total_crits += 1
    #    put the skill on cd
        self.remaining_cd = self.cooldown
        self.total_uses += 1
        self.total_dmg += skill_dmg
        
        char.current_focus -= self.focus_cost
        if char.current_focus > char.max_focus:
            char.current_focus = char.max_focus

        self.gcd_obj.wait_time = self.gcd_timer
        
        
        return skill_dmg
        
class SuperSunflower(skill):
    def __init__(self):
        self.name = "Super Sunflower"
    
    def cast(self, char, target):
#        TODO: Implement
        ap = char.attack_power
        crit = char.crit_rate
        cdmg = char.crit_damage
        ele = char.elemental
        ap_mod = self.ap_modifier
        for buf in char.buffs:
            ap += (buf.ap_buff * buf.stacks)
            crit += (buf.crit_buff * buf.stacks)
            cdmg += (buf.crit_dmg_buff * buf.stacks)
            ele += (buf.elemental_buff * buf.stacks)
            if buf.name == bracelet.name:
                ap_mod += 3.3
            
        for debuff in target.debuff:
            if debuff.name == poison.name:
                ap_mod += 1
                
    #    print(clock, ap)
        skill_dmg = random.uniform(ap_mod*(1-variance), ap_mod*(1+variance))*ap*ele
        if random.random() < crit:
            skill_dmg *= cdmg
            self.total_crits += 1
    #    put the skill on cd
        self.remaining_cd = self.cooldown
        self.total_uses += 1
        self.total_dmg += skill_dmg
        
        char.current_focus -= self.focus_cost
        if char.current_focus > char.max_focus:
            char.current_focus = char.max_focus
            
            
        for buff in char.buffs:
            if buff.name == photosynthesis.name:
                buff.stacks += 1
                if buff.stacks >= 5:
                    char.buffs.remove(buff)
                    for buff in buffs:
                        if buff.name == overflow.name:
                            buff.duration = buff.max_duration
                            break
                    else:
                        char.buffs.append(Buff(other=overflow))
            if buff.name == ssf_available.name:
                char.buffs.remove(buff)
            
        self.gcd_obj.wait_time = self.gcd_timer
        return skill_dmg
    

class Rosethorn(skill):
    def __init__(self):
        self.name = "Rosethorn"
    
    def cast(self, char):
#        TODO: Implement
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
        skill_dmg = random.uniform(self.ap_modifier*0.9, self.ap_modifier*1.1)*ap*ele
        if random.random() < crit:
            skill_dmg *= cdmg
            self.total_crits += 1
    #    put the skill on cd
        self.remaining_cd = self.cooldown
        self.total_uses += 1
        self.total_dmg += skill_dmg
        
        char.current_focus -= self.focus_cost
        if char.current_focus > char.max_focus:
            char.current_focus = char.max_focus

        self.gcd_obj.wait_time = self.gcd_timer
        return skill_dmg
    
class FlyingNettles(skill):
    def __init__(self):
        self.name = "Flying Nettles"
    
    def cast(self, char):
#        TODO: Implement
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
        skill_dmg = random.uniform(self.ap_modifier*0.9, self.ap_modifier*1.1)*ap*ele
        if random.random() < crit:
            skill_dmg *= cdmg
            self.total_crits += 1
    #    put the skill on cd
        self.remaining_cd = self.cooldown
        self.total_uses += 1
        self.total_dmg += skill_dmg
        
        char.current_focus -= self.focus_cost
        if char.current_focus > char.max_focus:
            char.current_focus = char.max_focus

        self.gcd_obj.wait_time = self.gcd_timer
        return skill_dmg
    
class BurrToss(skill):
    def __init__(self):
        self.name = "Burr Toss"
    
    def cast(self, char):
#        TODO: Implement
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
        skill_dmg = random.uniform(self.ap_modifier*0.9, self.ap_modifier*1.1)*ap*ele
        if random.random() < crit:
            skill_dmg *= cdmg
            self.total_crits += 1
    #    put the skill on cd
        self.remaining_cd = self.cooldown
        self.total_uses += 1
        self.total_dmg += skill_dmg
        
        char.current_focus -= self.focus_cost
        if char.current_focus > char.max_focus:
            char.current_focus = char.max_focus

        self.gcd_obj.wait_time = self.gcd_timer
        return skill_dmg
    
class GraspingRoots(skill):
    def __init__(self):
        self.name = "Grasping Roots"
    
    def cast(self, char):
#        TODO: Implement
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
        skill_dmg = random.uniform(self.ap_modifier*0.9, self.ap_modifier*1.1)*ap*ele
        if random.random() < crit:
            skill_dmg *= cdmg
            self.total_crits += 1
    #    put the skill on cd
        self.remaining_cd = self.cooldown
        self.total_uses += 1
        self.total_dmg += skill_dmg
        
        char.current_focus -= self.focus_cost
        if char.current_focus > char.max_focus:
            char.current_focus = char.max_focus

        self.gcd_obj.wait_time = self.gcd_timer
        return skill_dmg
    
class PetalStormToss(skill):
    def __init__(self):
        self.name = "Petal Storm Toss"
    
    def cast(self, char):
#        TODO: Implement
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
        skill_dmg = random.uniform(self.ap_modifier*(1-variance), self.ap_modifier*(1+variance))*ap*ele
        if random.random() < crit:
            skill_dmg *= cdmg
            self.total_crits += 1
    #    put the skill on cd
        self.remaining_cd = self.cooldown
        self.total_uses += 1
        self.total_dmg += skill_dmg
        
        char.current_focus -= self.focus_cost
        if char.current_focus > char.max_focus:
            char.current_focus = char.max_focus
        
        self.gcd_obj.wait_time = self.gcd_timer
        return skill_dmg
    
