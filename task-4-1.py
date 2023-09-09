class villain:
    def __init__(self,health,energy):
        self.health = health
        self.energy = energy
class GRU(villain):
    weapon_damage=0
    shield_save=0
    weapon=0
    shield=0
    w2=5
    w3=3
    w4=1
    s2=2
    def __init__(self,health,energy):
        super().__init__(health,energy)
    def choose_weapon(self):
        print("------------------------------------------------------")
        print("CHOOSE GRU WEAPONS:")
        if int(self.energy) >=120:
            print("available weapons:\n1-freeze gun\t2-electric prod\t3-mega magnet\t4-kalmen missile\t5-No weapon")
            self.weapon = input("Enter Your Choice: ")
        elif int(self.energy) >=92:
            print("available weapons:\n1-freeze gun\t2-electric prod\t3-mega magnet\t5-no weapon")
            self.weapon = input("Enter Your Choice: ")
        elif int(self.energy) >=88:
            print("available weapons:\n1-freeze gun\t2-electric prod\t5-no weapon")
            self.weapon = input("Enter Your Choice: ")
        elif int(self.energy) >=50:
            print("available weapons:\n1-freeze gun\t5-no weapon")
            self.weapon = input("Enter Your Choice: ")
        else:
            print("no weapon")
            self.weapon=5
        print("------------------------------------------------------")
        GRU.weapon_energy(self)
    def weapon_energy(self):
        if int(self.weapon) == 1:
            if(self.energy>=50):
                self.energy -= 50
                GRU.weapon_damage = 11
            else:
                print("no enough energy")
        elif int(self.weapon) == 2:
            self.w2=GRU.weapon_resources(self,self.w2)
            if(self.energy>=88):
                self.energy -= 88
                GRU.weapon_damage = 18
            else:
                print("no enough energy")
                GRU.choose_weapon(self)
        elif int(self.weapon) == 3:
            self.w3=GRU.weapon_resources(self,self.w3)
            if(self.energy>=92):
                self.energy -= 92
                GRU.weapon_damage = 10
            else:
                print("no enough energy")
                GRU.choose_weapon(self)
        elif int(self.weapon) == 4:
            self.w4=GRU.weapon_resources(self,self.w4)
            if(self.energy>=120):
                self.energy -= 120
                GRU.weapon_damage = 20
            else:
                print("no enough energy")
                GRU.choose_weapon(self)
        elif int(self.weapon)==5:
            self.energy -= 0
            GRU.weapon_damage = 0
        else :
            print("------------------------------------------------------")
            print("NOT AVAILABLE")
            print("------------------------------------------------------")
            GRU.choose_weapon(self)
    def weapon_resources(self,x):
        if(x==0):
            print("------------------------------------------------------")
            print("you can't use that weapon...please chose another one")
            print("------------------------------------------------------")
            GRU.choose_weapon(self)
        else:
            return x-1 
    def choose_shield(self):
        print("------------------------------------------------------")
        print("CHOOSE GRU SHIELD:")
        if int(self.energy) >= 50 :
            print("available shields:\n1-energy projected barrier gun\t2-selective permeability\t3-no shield")
            self.shield = input("Enter Your Choice: ")
        elif int(self.energy) >= 20:
            print("available shields:\n1-energy projected barrier gun\t3-no shield")
            self.shield = input("Enter Your Choice: ")
        else:
            print("------------------------------------------------------")
            print("No shield")
            print("------------------------------------------------------")
            self.shield=3
        print("------------------------------------------------------")
        GRU.shield_energy(self)
    def shield_energy(self):
        if int(self.shield) == 1:
            if(self.energy>=20):
                self.energy -= 20
                GRU.shield_save = 0.6
        elif int(self.shield) == 2:
            self.s2=GRU.shield_resources(self,self.s2)
            if(self.energy>=50):
                self.energy -= 50
                GRU.shield_save = 0.1
        elif int(self.shield)==3:
            self.energy -= 0
            GRU.shield_save = 1
        else:
            print("no shield available")
            GRU.choose_shield(self)
    def shield_resources(self,x):
        if(x==0):
            print("------------------------------------------------------")
            print("you can't use that weapon...please chose another one")
            print("------------------------------------------------------")
            GRU.choose_shield(self)
        else:
            return x-1 
class VECTOR(villain):
    weapon_damage=0
    shield_save=0
    weapon=0
    shield=0
    w2=8
    w3=3
    s2=3
    def __init__(self,health,energy):
        super().__init__(health,energy)
    def choose_weapon(self):
        print("------------------------------------------------------")
        print("CHOOSE VECTOR WEAPON:")
        if int(self.energy) >=100:
            print("available weapons:\n1-laser blaster\t2-plasma grenades\t3-sonic reasonance cannon\t4-no weapon")
            self.weapon = input("Enter Your Choice: ")
        elif (self.energy) >=56:
            print("available weapons:\n1-laser blaster\t2-plasma grenades\t4-no weapon")
            self.weapon = input("Enter Your Choice: ")
        elif (self.energy) >=40:
            print("available weapons:\n1-laser blaster\t 4-no weapon")
            self.weapon = input("Enter Your Choice: ")
        else:
            print("------------------------------------------------------")
            print("No weapon")
            print("------------------------------------------------------")
            self.weapon=4
        print("------------------------------------------------------")
        VECTOR.weapon_energy(self)
    def weapon_energy(self):
        if int(self.weapon) == 1:
            if self.energy>=40:
                self.energy -= 40
                VECTOR.weapon_damage = 8
        elif int(self.weapon) == 2:
            self.w2=VECTOR.weapon_resources(self,self.w2)
            if self.energy>=56:
                self.energy -= 56
                VECTOR.weapon_damage = 13
        elif int(self.weapon) == 3:
            self.w3=VECTOR.weapon_resources(self,self.w3)
            if self.energy>=100:
                self.energy -= 100
                VECTOR.weapon_damage = 22
        elif int(self.weapon) == 4:
            self.energy-=0
            VECTOR.weapon_damage=0
        else:
            print("------------------------------------------------------")
            print("no weapon available")
            print("------------------------------------------------------")
            VECTOR.choose_weapon(self)
    def weapon_resources(self,x):
        if(x==0):
            print("------------------------------------------------------")
            print("you can't use that weapon...please chose another one")
            print("------------------------------------------------------")
            VECTOR.choose_weapon(self)
        else:
            return x-1 
    def choose_shield(self):
        print("------------------------------------------------------")
        print("CHOOSE VECTOR SHIELD:")
        if int(self.energy) >= 40 :
            print("available shields:\n1-energy net trap\t2-quantum deflector\t3-no shield")
            self.shield = input("Enter Your Choice: ")
        elif int(self.energy) >= 15:
            print("available shields:\n1-energy net trap\t3-no shield")
            self.shield = input("Enter Your Choice: ")
        else:
            print("------------------------------------------------------")
            print("No shield")
            print("------------------------------------------------------")
            self.shield = 3
        print("------------------------------------------------------")
        VECTOR.shield_energy(self)
    def shield_energy(self):
        if int(self.shield) == 1:
            if self.energy>=15:
                self.energy -= 15
                VECTOR.shield_save = 0.68
        elif int(self.shield) == 2:
            self.s2=VECTOR.shield_resources(self,self.s2)
            if self.energy>=40:
                self.energy -= 40
                VECTOR.shield_save = 0.2
        elif int(self.shield)==3:
            self.energy-=0
            VECTOR.shield_save=1
        else:
            print("------------------------------------------------------")
            print("no shield available")
            print("------------------------------------------------------")
            VECTOR.choose_shield(self)
    def shield_resources(self,x):
        if(x==0):
            print("------------------------------------------------------")
            print("you can't use that shield...please chose another one")
            print("------------------------------------------------------")
            VECTOR.choose_shield(self)
        else:
            return x-1 
def actual_damage():
    if int(villian1.weapon) == 4 :
        villian2.health -= villian1.weapon_damage
        villian1.health -= villian1.shield_save*villian2.weapon_damage
    elif int(villian1.weapon) == 3:
        villian1.health -= villian2.weapon_damage * 0.8
        villian2.health -= villian2.shield_save*villian1.weapon_damage
    else:
        villian1.health -= villian1.shield_save*villian2.weapon_damage
        villian2.health -= villian2.shield_save*villian1.weapon_damage

    
villian1=GRU(100,500)
villian2=VECTOR(100,500)  
while (villian1.energy>15 or villian2.energy>20) and (villian1.health>0 and villian2.health>0):
    villian1.choose_weapon()
    villian1.choose_shield()
    villian2.choose_weapon()
    villian2.choose_shield()
    actual_damage() 
    print("--------------------------------------------")
    print(f"GRU health:={villian1.health}")
    print(f"VECTOR health:={villian2.health}")
    print(f"GRU energy:={villian1.energy}")
    print(f"VECTOR energy:={villian2.energy}")
    print("--------------------------------------------")
if villian1.health<=0:
    print("Vector won!!")
elif villian2.health<=0:
    print("GRU won!!")
else:
    print("DRAW!!")