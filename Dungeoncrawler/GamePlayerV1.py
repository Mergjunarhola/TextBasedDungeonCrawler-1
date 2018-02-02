#Lokaverkefni For3
#Höfundur: Jón Benediktsson
#dags: 27.12.2017

from ctypes import *
from random import randint
import color_console as cons
import sys

#linkar

#Print here commandið
#https://rosettacode.org/wiki/Terminal_control/Cursor_positioning#Python

#litir
#https://www.burgaud.com/bring-colors-to-the-windows-console-with-python/

#"bitwise or"
#https://wiki.python.org/moin/BitwiseOperators



default_colors = cons.get_text_attr()
default_bg = default_colors & 0x0070
default_fg = default_colors & 0x0007
class COORD(Structure):
    pass


COORD._fields_ = [("X", c_short), ("Y", c_short)]


def print_at(r, c, s):
    h = windll.kernel32.GetStdHandle(-11)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))

    c = s.encode("UTF-8")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)



#=================================================================
#                        minn kóði
#=================================================================

#color format til að geta haldið í vissa liti fyrir vissa hluti
class Color_Form():
    def __init__(self, *args):
        TempBin=0x0000                      #ég reyndi að læra aðeins á þetta og ég bara fatta ekki hvað þetta þýðir
        for x in args:                      #það á að vera einhverskonar binary number hlutur eða eithvað
            TempBin=(TempBin|x)             #og þetta hér á að gera "bitwise or" ég náði þessu samt til að virka
        self.__Color__=TempBin
    def GetColor(self):
        return self.__Color__



#Standard fyrir munstrið á borderinum

#0-1-2
#|   |
#7 8 3
#|   |
#6-5-4

#þetta gerir þannig"╔═╗║╝═╚║ "
#þetta
#╔═╗
#║ ║
#╚═╝

RandomEn=[["Ananas",5,1,-10,5],["Snakur",10,3,1,20],["Dvergur",30,5,-1,100]]






class kassi():
    def __init__(self,LiturBorder,LiturInni,X,Y,Breydd,Haed,Munstur):
        self.LiturBorder=LiturBorder
        self.LiturInni=LiturInni
        self.X=Y
        self.Y=X
        self.Breydd=Haed    #það var einhver villa í þessu hjá mér svo ég bara víxlaði því
        self.Haed=Breydd    #print at gerir y svo x í stað x,y það er vandamálið
        self.Munstur=Munstur

    def teikna(self):
        PH="0"    #heldur um munstrið sem á að prenta eða Print Holder
        Litur=0x0000       #heldur um litin sem á að nota
        for x in range(self.Breydd):
            for y in range(self.Haed):
                if x+y==0:                                      #0
                    PH=self.Munstur[0]
                    Litur=self.LiturBorder
                elif  y == self.Haed-1 and x ==0:               #2
                    PH = self.Munstur[2]
                    Litur = self.LiturBorder
                elif  x == self.Breydd-1 and y ==0:             #4
                    PH = self.Munstur[4]
                    Litur = self.LiturBorder
                elif  x == self.Breydd-1 and y == self.Haed-1:  #6
                    PH = self.Munstur[6]
                    Litur = self.LiturBorder
                elif y==0:                                      #7
                    PH = self.Munstur[7]
                    Litur = self.LiturBorder
                elif x==self.Breydd-1:                          #5
                    PH = self.Munstur[5]
                    Litur = self.LiturBorder
                elif y==self.Haed-1:                            #3
                    PH = self.Munstur[3]
                    Litur = self.LiturBorder
                elif x==0:                                      #1
                    PH = self.Munstur[1]
                    Litur = self.LiturBorder
                else:                                           #8
                    PH = self.Munstur[8]
                    Litur = self.LiturInni

                cons.set_text_attr(Litur)
                print_at((self.X+x),(self.Y+y),PH)





#litir sem eru notaðir í kassana á skjánum og fleyrra
Grunnur= Color_Form(default_bg,default_fg)
Border= Color_Form(cons.FOREGROUND_BLACK,cons.BACKGROUND_GREY)
StatsColor=Color_Form(default_bg,cons.FOREGROUND_MAGENTA)
CommandColor=Color_Form(default_bg,cons.FOREGROUND_RED)

#samsetninginn og teknuninn á menuinu
MainBack=kassi(Border.GetColor(),Border.GetColor(),0,0,120,47,"0-0|0-0| ")
MainBack.teikna()
MainPlay=kassi(Border.GetColor(),Grunnur.GetColor(),5,2,61,32,"0-0|0-0| ")
MainPlay.teikna()
StatsBox=kassi(StatsColor.GetColor(),Grunnur.GetColor(),80,3,20,30,"0-0|0-0| ")
StatsBox.teikna()
CommandBox=kassi(CommandColor.GetColor(),Grunnur.GetColor(),7,35,59,8,"0-0|0-0| ")
CommandBox.teikna()
CTLoc=[37,9] #command retun location
print_at(0,0,"")
input()

class Character():
    def __init__(self,Nafn,MaxHp,Str,Dex,Vopn,Def,Agi,Int):
        self._Nafn=Nafn
        self._MaxHp=MaxHp
        self._Str=Str
        self._Dex=Dex
        self._Vopn=Vopn
        self._Def=Def
        self._Agi=Agi
        self._Int=Int
        self._Peningar=0
        self._lookrange=5
        self._Hp=MaxHp
    def AddMoney(self,Ammount):
        self._Peningar=self._Peningar+Ammount
    def Money(self):
        return self._Peningar
    def Look(self):
        return self._lookrange
    def Attack(self):
        return self._Vopn.Dmg()
    def Recive_Damage(self,Damage):
        if Damage > self._Def:
            pass
        else:
            self._Hp=self._Hp-Damage+self._Def
    def Print_Stats(self):
        cons.set_text_attr(default_colors)
        print_at(4,89-(len("Hp: "+str(self._Hp)+"/"+str(self._MaxHp))//2),"Hp: "+str(self._Hp)+"/"+str(self._MaxHp))
        health_bar="<|==============|>"
        cons.set_text_attr(default_bg|cons.FOREGROUND_GREEN)
        print_at(5, 81 ,health_bar)
        if self._Hp<self._MaxHp:
            cons.set_text_attr(default_bg|cons.BACKGROUND_RED)
            print_at(4, 90 ,"|>")

class items():
    def __init__(self,verd,typa):
        self._verd=verd
        self._typa=typa
    def GetType(self):
        return self._typa
    def GetWorth(self):
        return self._verd


class Vopn(items):
    def __init__(self,Drif,Dmg,Virdi):
        items.__init__(self,Virdi,"Vopn")
        self._Drif=Drif
        self._Dmg=Dmg
    def Drif(self):
        return self._Drif
    def Dmg(self):
        return self._Dmg

class Enemy():
    def __init__(self,Nafn,Hp,Dmg,Agi,Gold):
        self._Nafn=Nafn
        self._Stafur=Nafn[0]
        self._Hp=Hp
        self._Dmg=Dmg
        self._Agi=Agi
        self._Gold=Gold
        self._seen=False
        self._Dead=False
    def GetAgi(self):
        return self._Agi
    def GetStafur(self):
        return self._Stafur
    def IsDead(self):
        return self._Dead
    def Loot(self):
        goldcar=int(self._Gold)
        self._Gold=0
        return goldcar
    def Recive_Damage(self,Damage):
        self._Hp=self._Hp-Damage
        if self._Hp<1:
            self._Dead=True
            CTL("Thu drapst eithvad sem bar nafnid "+self._Nafn)
        else:
            CTL("Thu gerdir aras a eithvad sem ber nafnid " + self._Nafn)
    def Attack(self):
        return self._Dmg


Grasyda=Vopn(1,4,70)
Anton=Character("Anton",20,2,2,Grasyda,1,1,0)

class Map():
    def __init__(self,File):
        self._enemypos=[]
        self._itempos=[]
        self._Characterpos=[]
        self._Enemies=[]
        #þarf að laga þetta seinna svo þetta sé ekki eins mikið klusterfuck

        skra=open(File,"r",encoding="UTF-8")
        tempCopy=skra.read()
        skra.close()
        tempcopyx=tempCopy.split("\n")
        self._Holder=[]#þetta heldur mappinu
        for y in range(len(tempcopyx)):
            self._Holder.append([])
            for x in range(len(tempcopyx[y])):
                self._Holder[y].append(tempcopyx[y][x])
                if tempcopyx[y][x]=="E":
                    self._enemypos.append([x,y])
                    RaChoice=RandomEn[randint(0,len(RandomEn)-1)]#les random enemy úr listanum
                    self._Enemies.append(Enemy(RaChoice[0],RaChoice[1],RaChoice[2],RaChoice[3],RaChoice[4]))
                    self._Holder[y][x]="."
                if tempcopyx[y][x]=="I":
                    self._itempos.append([x,y])
                    self._Holder[y][x] = "."
                if tempcopyx[y][x]=="S":
                    self._Characterpos=[x,y]
                    self._Holder[y][x] = "."
    def searchOnscreen(self,dist,listi):
        outp=[]
        for x in range(len(listi)):
            if listi[x][0] in range(self._Characterpos[0]-dist,self._Characterpos[0]+dist) and  listi[x][1] in range(self._Characterpos[1]-dist,self._Characterpos[1]+dist):
                outp.append(x)
        return outp

    def draw(self):
        WallColor=Color_Form(cons.FOREGROUND_INTENSITY,cons.FOREGROUND_GREY,cons.BACKGROUND_INTENSITY,cons.BACKGROUND_RED)
        EnemyColor=Color_Form(cons.FOREGROUND_RED,default_bg)
        ItemColor = Color_Form(cons.FOREGROUND_YELLOW, default_bg)
        CharacterColor = Color_Form(cons.FOREGROUND_CYAN, default_bg)
        for x in range(0,30):
            for y in range(0,30):
                if self._Holder[y+self._Characterpos[1]-15][x+self._Characterpos[0]-15]=="#":
                    cons.set_text_attr(WallColor.GetColor())
                else:
                    cons.set_text_attr(default_colors)
                print_at(3+y,6+(x*2),self._Holder[y+self._Characterpos[1]-15][x+self._Characterpos[0]-15])
        EnemyOnscreen=self.searchOnscreen(15,self._enemypos)
        ItemOnscreen = self.searchOnscreen(15, self._itempos)
        cons.set_text_attr(EnemyColor.GetColor())
        for x in EnemyOnscreen:
            print_at(18-(self._Characterpos[1]-self._enemypos[x][1]),36-(2*(self._Characterpos[0]-self._enemypos[x][0])),self._Enemies[x].GetStafur())
        cons.set_text_attr(ItemColor.GetColor())
        for x in ItemOnscreen:
            print_at(18-(self._Characterpos[1]-self._itempos[x][1]),36-(2*(self._Characterpos[0]-self._itempos[x][0])),"I")
        cons.set_text_attr(CharacterColor.GetColor())
        print_at(18,36,"@")

    def Action(self,command):
        testloc=list(self._Characterpos)
        if command== "w":
            testloc[1]=testloc[1]-1
        elif command== "s":
            testloc[1]=testloc[1]+1
        elif command== "a":
            testloc[0]=testloc[0]-1
        elif command== "d":
            testloc[0]=testloc[0]+1

        if self._Holder[testloc[1]][testloc[0]]=="#":
            CTL("thad er eithvad fyrir ther")
            return False
        elif testloc in self._enemypos:
            EnemyId=self._enemypos.index(testloc)
            if self._Enemies[EnemyId].IsDead():
                Gold=int(self._Enemies[EnemyId].Loot())
                if Gold==0:
                    self._Characterpos=testloc
                else:
                    Anton.AddMoney(Gold)
                    CTL("thu fanst "+str(Gold)+" kronur a likinu")
            else:
                self._Enemies[EnemyId].Recive_Damage(Anton.Attack())
            return True
        else:
            self._Characterpos=testloc
            return True
def CTL(message):
    cons.set_text_attr(CommandColor.GetColor())
    print_at(CTLoc[0], CTLoc[1], "                                                        ")
    print_at(CTLoc[0], CTLoc[1], message)
    cons.set_text_attr(cons.FOREGROUND_CYAN | default_bg)
    print_at(CTLoc[0] + 1, CTLoc[1], "                                                        ")
    print_at(CTLoc[0] + 1, CTLoc[1], "")
Leikur=Map("Test_2.txt")

def CTI(Message):
    cons.set_text_attr(cons.FOREGROUND_YELLOW | default_bg)
    print_at(CTLoc[0] -1, CTLoc[1], "                                                        ")
    print_at(CTLoc[0] -1, CTLoc[1], "")


class Turns():
    def __init__(self,EnemyList):
        self._ind = 0
        self._Turnlist=[]
        for x in range(21):
            self._Turnlist.append(["filler"])
        self._Turnlist[0].append("C")
        for x in range(len(EnemyList)):
            self._Turnlist[randint(1,20)].append(x)
    def GetTurn(self):
        if len(self._Turnlist[0])<=self._ind:
            self._ind = 0
            for x in range(20):
                self._Turnlist[x]=self._Turnlist[x+1]
            self._Turnlist[20] = ["filler"]
        self._ind = self._ind +1
        return self._Turnlist[0][self._ind-1]
    def SetTurn(self,hlutur,Agi):
        self._Turnlist[10-Agi].append(hlutur)




Rodinn=Turns(Leikur._Enemies)
Trust=False
#hér birjar leikurinn að gera hluti
while True:
    while not Trust:
        Anton.Print_Stats()
        Leikur.draw()
        print_at(CTLoc[0] + 1, CTLoc[1], "                                                        ")
        print_at(CTLoc[0] + 1, CTLoc[1], "")
        inp=input()
        if "/" in inp:
            pass
        elif inp in "asdw":
            Trust=Leikur.Action(inp)

    Rodinn.SetTurn("C",Anton._Agi)
    while Trust:
        Onscreen=Leikur.searchOnscreen(10,Leikur._enemypos)
        Engaged=Leikur.searchOnscreen(2,Leikur._enemypos)
        Gera=Rodinn.GetTurn()

        if Gera=="C":
            Trust=False
        elif Gera=="filler":
            pass
        elif Leikur._Enemies[Gera].IsDead():
            pass
        else:
            if Gera in Onscreen:
                if Gera in Engaged:
                    Anton.Recive_Damage(Leikur._Enemies[Gera].Attack())
                else:
                    if Leikur._enemypos[Gera][1]==Leikur._Characterpos[1]:
                        if Leikur._enemypos[Gera][0]>Leikur._Characterpos[0]:
                            tempdir=-1
                        else:
                            tempdir=1
                        Leikur._enemypos[Gera][0]=Leikur._enemypos[Gera][0]+tempdir
                    if Leikur._enemypos[Gera][0]==Leikur._Characterpos[0]:
                        if Leikur._enemypos[Gera][1]>Leikur._Characterpos[1]:
                            tempdir=-1
                        else:
                            tempdir=1
                        Leikur._enemypos[Gera][1]=Leikur._enemypos[Gera][1]+tempdir
                    else:
                        randdir=randint(0,1)
                        if randdir==0:
                            if Leikur._enemypos[Gera][0] > Leikur._Characterpos[0]:
                                tempdir = -1
                            else:
                                tempdir = 1
                        else:
                            if Leikur._enemypos[Gera][1] > Leikur._Characterpos[1]:
                                tempdir = -1
                            else:
                                tempdir = 1

                        Leikur._enemypos[Gera][randdir] = Leikur._enemypos[Gera][randdir] + tempdir
            else:
                randdir = randint(0, 1)
                randdir2= randint(0, 1)
                Leikur._enemypos[Gera][randdir] = Leikur._enemypos[Gera][randdir] + [-1,1][randdir2]
            Rodinn.SetTurn(Gera,Leikur._Enemies[Gera].GetAgi())

































