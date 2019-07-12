# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 23:00:29 2018

@author: Noah G
"""
import random
from buff import *
from gcd_object import gcd_object

class skill:
    
    def __init__(self, ap_mod = 1, gcd_time = 1, focus_cost = 0, cd = 1, gcd=None, name=""):
        self.ap_modifier = ap_mod
        self.gcd_timer = gcd_time
        self.total_uses = 0
        self.total_crits = 0
        self.focus_cost = focus_cost
        self.cooldown = cd
        self.remaining_cd = 0
        self.total_dmg = 0
        self.gcd_obj = gcd
        self.name = name
        self.variance = 0.1
        
    def can_use(self):
        print("Base case")
    
class ThornStrike(skill): 
        
    def can_use(self, char, target):
        return all([self.focus_cost <= char.current_focus, self.gcd_obj.wait_time<=0,
                    self.remaining_cd <=0])
        
    def cast(self, char, target):
#        TODO: Implement
        
        ap, ele, crit, cdmg = char.get_stats()
        ap_mod = self.ap_modifier
        self.remaining_cd = self.cooldown
        for buf in char.buffs:
            if buf.name == dynasty.name:
                ap_mod += 8
                self.remaining_cd = 0
                buf.stacks -= 1
            
        for debuff in target.debuffs:
            if debuff.name == poison.name:
                ap_mod +=6.5
                debuff.remaining += 6
                if debuff.remaining > debuff.max_duration:
                    debuff.remaining = debuff.max_duration
        
        for sk in char.skills:
            if sk.name == flying_nettles.name:
                sk.remaining_cd -= 1.5
        
        
        skill_dmg = random.uniform(ap_mod*(1-self.variance), ap_mod*(1+self.variance))*ap*ele
        if random.random() < crit:
            skill_dmg *= cdmg
            self.total_crits += 1
    #    put the skill on cd
        self.total_uses += 1
        self.total_dmg += skill_dmg
        
        char.current_focus -= self.focus_cost
        if char.current_focus > char.max_focus:
            char.current_focus = char.max_focus

        buff_names = [buff.name for buff in char.buffs]
        if not magnum_final.name in buff_names:
            for buff in char.buffs:
                if buff.name == magnum.name:
                    buff.stacks += 1
                    if buff.stacks == 3:
                        char.buffs.remove(buff)
                        char.buffs.append(Buff(other=magnum_final))
                        break
            else:
                char.buffs.append(Buff(other=magnum))
        
        return skill_dmg
    
class Sunflower(skill):
        
    def can_use(self, char, target):
        return all([self.focus_cost <= char.current_focus, self.gcd_obj.wait_time<=0,
                    self.remaining_cd <=0])
    
    def cast(self, char, target):
        ap = char.attack_power
        crit = char.crit_rate
        cdmg = char.crit_damage
        ele = char.elemental
        ap_mod = self.ap_modifier
        
        for db in target.debuffs:
            if db.name == poison.name:
                ap_mod += 1
                char.buffs.append(Buff(other=ssf_available))
                
        for buf in char.buffs:
            ap += (buf.ap_buff * buf.stacks)
            crit += (buf.crit_buff * buf.stacks)
            cdmg += (buf.crit_dmg_buff * buf.stacks)
            ele += (buf.elemental_buff * buf.stacks)
            if buf.name == bracelet.name:
                ap_mod += 3.3
            
    #    print(clock, ap)
        skill_dmg = random.uniform(ap_mod*(1-self.variance), ap_mod*(1+self.variance))*ap*ele
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
        
    def can_use(self, char, target):
        return all([self.focus_cost <= char.current_focus, self.gcd_obj.wait_time<=0,
                    self.remaining_cd <=0, any([True for buff in char.buffs 
                                                if buff.name == overflow.name or
                                                buff.name == ssf_available.name])])
    
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
            
        for debuff in target.debuffs:
            if debuff.name == poison.name:
                ap_mod += 1
                
    #    print(clock, ap)
        c_flag = False
        skill_dmg = random.uniform(ap_mod*(1-self.variance), ap_mod*(1+self.variance))*ap*ele
        if random.random() < crit:
            skill_dmg *= cdmg
            self.total_crits += 1
            c_flag = True
    #    put the skill on cd
        self.remaining_cd = self.cooldown
        self.total_uses += 1
        self.total_dmg += skill_dmg
        
        char.current_focus -= self.focus_cost
        if char.current_focus > char.max_focus:
            char.current_focus = char.max_focus
            
        if c_flag:
            for sk in char.skills:
                if sk.name == thorn_strike.name:
                    sk.remaining_cd -= 3
        
        
        for buff in char.buffs:
            if buff.name == photosynthesis.name:
                buff.stacks += 1
                if buff.stacks >= 5:
                    char.buffs.remove(buff)
                    for buff in char.buffs:
                        if buff.name == overflow.name:
                            buff.duration = buff.max_duration
                            break
                    else:
                        char.buffs.append(Buff(other=overflow))
                continue
            if buff.name == ssf_available.name:
                char.buffs.remove(buff)
        else:
            char.buffs.append(Buff(other=photosynthesis))
        self.gcd_obj.wait_time = self.gcd_timer
        return skill_dmg
    

class Rosethorn(skill):
        
    def can_use(self, char, target):
        return all([self.gcd_obj.wait_time<=0, self.remaining_cd <=0])
    
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
            
    #    print(clock, ap)
        skill_dmg = random.uniform(ap_mod*(1-self.variance), ap_mod*(1+self.variance))*ap*ele
        c_flag = False
        if random.random() < crit:
            skill_dmg *= cdmg
            self.total_crits += 1
            c_flag = True
    #    put the skill on cd
        self.remaining_cd = self.cooldown
        self.total_uses += 1
        self.total_dmg += skill_dmg
        
        char.current_focus -= self.focus_cost
        if c_flag:
            char.current_focus += 2
        if char.current_focus > char.max_focus:
            char.current_focus = char.max_focus

        self.gcd_obj.wait_time = self.gcd_timer
        return skill_dmg
    
class FlyingNettles(skill):
        
    def can_use(self, char, target):
        return all([self.focus_cost <= char.current_focus, self.gcd_obj.wait_time<=0,
                    self.remaining_cd <=0, any([True for db in target.debuffs if db.name == poison.name])])
    
    def cast(self, char, target):
        ap, ele, crit, cdmg= char.get_stats()
        ap_mod = self.ap_modifier
        
        for db in target.debuffs:
            if db.name == poison.name:
                ap_mod += self.ap_modifier
                
        init_dmg = ap_mod/5
                
        for buf in char.buffs:
            if buf.name == magnum_final.name:
                init_dmg +=69.3
                char.buffs.remove(buf)
        
        
            
    #    print(clock, ap)
        skill_dmg = random.uniform(init_dmg*(1-self.variance), init_dmg*(1+self.variance))*ap*ele
        if random.random() < crit:
            skill_dmg *= cdmg
            self.total_crits += 1
    #    put the skill on cd
        self.remaining_cd = self.cooldown
        self.total_uses += 1
        self.total_dmg += skill_dmg
        
        target.debuffs.append(Debuff(duration = 10, damage = ap_mod/5, tick = 2, name = "Flying Nettles DoT"))
        
        for sk in char.skills:
            if sk.name == thorn_strike.name:
                sk.remaining_cd = 0
        
        
        char.current_focus -= self.focus_cost
        if char.current_focus > char.max_focus:
            char.current_focus = char.max_focus

        char.buffs.append(Buff(other=dynasty))
        self.gcd_obj.wait_time = self.gcd_timer
        return skill_dmg
    
class BurrToss(skill):
        
    def can_use(self, char, target):
        return all([self.focus_cost <= char.current_focus, self.gcd_obj.wait_time<=0,
                    self.remaining_cd <=0, any([True for buff in char.buffs if
                                                buff.name == burr_available.name])])
    
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
            
    #    print(clock, ap)
        skill_dmg = random.uniform(ap_mod*(1-self.variance), ap_mod*(1+self.variance))*ap*ele
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
        
    def can_use(self, char, target):
        return all([self.focus_cost <= char.current_focus, self.gcd_obj.wait_time<=0,
                    self.remaining_cd <=0])
    
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
            
    #    print(clock, ap)
        skill_dmg = random.uniform(ap_mod*(1-self.variance), ap_mod*(1+self.variance))*ap*ele
        if random.random() < crit:
            skill_dmg *= cdmg
            self.total_crits += 1
    #    put the skill on cd
        self.remaining_cd = self.cooldown
        self.total_uses += 1
        self.total_dmg += skill_dmg
        
        for db in target.debuffs:
            if db.name == poison.name:
                db.duration = db.max_duration
                break
        else:
            target.debuffs.append(Debuff(duration = 10, damage = 0.6, tick = 1, name = "Ivy Poison"))
        
        char.current_focus -= self.focus_cost
        if char.current_focus > char.max_focus:
            char.current_focus = char.max_focus

        self.gcd_obj.wait_time = self.gcd_timer
        return skill_dmg
    
class PetalStormToss(skill):
        
    def can_use(self, char, target):
        return all([self.focus_cost <= char.current_focus, self.gcd_obj.wait_time<=0,
                    self.remaining_cd <=0])
    
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
            
    #    print(clock, ap)
        skill_dmg = random.uniform(ap_mod*(1-self.variance), ap_mod*(1+self.variance))*ap*ele
        if random.random() < crit:
            skill_dmg *= cdmg
            self.total_crits += 1
    #    put the skill on cd
        self.remaining_cd = self.cooldown
        self.total_uses += 1
        self.total_dmg += skill_dmg
        
        for buff in char.buffs:
            if buff.name == bracelet.name:
                buff.duration = buff.max_duration
                break
        else:
            char.buffs.append(Buff(other = bracelet))
        
        char.current_focus -= self.focus_cost
        if char.current_focus > char.max_focus:
            char.current_focus = char.max_focus
        
        self.gcd_obj.wait_time = self.gcd_timer
        return skill_dmg
    


gcd1 = gcd_object()
gcd2 = gcd_object()
gcd3 = gcd_object()

rosethorn = Rosethorn(ap_mod=1.75, gcd_time=0.4, focus_cost=-1, cd=0.4, gcd=gcd1, name = "Rosethorn")
sunflower = Sunflower(ap_mod=4.8, gcd_time=0.5, focus_cost=3, cd=0.5, gcd=gcd2, name = "Sunflower")
super_sunflower = SuperSunflower(ap_mod=7.7, gcd_time=0.5, focus_cost=2, cd=0.5, gcd=gcd2, name = "Super Sunflower")
thorn_strike = ThornStrike(ap_mod=5.5, gcd_time=1, focus_cost=2, cd=18, gcd=gcd3, name = "Thorn Strike")
#    Doom_bloom = skill("doom and bloom", 6.4, 1, 0, 18)
flying_nettles = FlyingNettles(ap_mod=34.65, gcd_time=1, focus_cost=0, cd=10.4, gcd=gcd3, name = "Flying Nettles")
grasping_roots = GraspingRoots(ap_mod=7.5, gcd_time=0.5, focus_cost=2, cd=24, gcd=gcd3, name = "Grasping Roots")
petal_storm = PetalStormToss(ap_mod=20, gcd_time=1, focus_cost=2, cd=24, gcd=gcd3, name = "Petal Storm Toss")
burr_toss = BurrToss(ap_mod=90, gcd_time=1, focus_cost=0, cd=0, gcd=gcd3, name = "Burr Toss")
