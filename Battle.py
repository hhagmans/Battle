import random

def Angriff(angreifer,verteidiger):
    ausweichen = angreifer.geschicklichkeit - verteidiger.geschicklichkeit
    if ausweichen <= 0:
        ausweichen = 1
    if random.randint(1,100) > ausweichen:
        schaden = angreifer.angriff - verteidiger.verteidigung + random.randint(-verteidiger.verteidigung,angreifer.angriff)
        if schaden <= 0:
            schaden = 1
    else:
        print "Ausgewichen!"
        schaden = 0
    return schaden
        
        
def ItemUse(item):
    if item.typ == "Energie":
        return [E,item.wert]
    elif item.typ == "Mana":
        return [M,item.wert]
    else:
        print "Item bisher nicht benutzbar"
        
