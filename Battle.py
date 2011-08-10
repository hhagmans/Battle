import Items,time,pygame,random
from pygame.locals import *

def Angriff(angreifer,verteidiger):
    """Schadensberechnung bei Angriff, eventuell weicht der Verteidiger aus"""
    ausweichen = verteidiger.geschicklichkeit - angreifer.geschicklichkeit
    if ausweichen <= 0:
        ausweichen = 1                              # Auseichwahrscheinlichkeit
    if random.randint(1,100) > ausweichen:
        schaden = angreifer.angriff - verteidiger.verteidigung + random.randint(-verteidiger.verteidigung,angreifer.angriff)    # Schadensberechnung
        if schaden <= 0:
            schaden = 1
    else:
        print "Ausgewichen!"
        schaden = 0
    return schaden
        
        
def ItemUse(item):
    """ Prueftden Typ des uebergebenen Items und gibt dann je nach Typ einen Wert zurueck"""
    if item.typ == "Energie":
        return item.wert
    elif item.typ == "Mana":
        return item.wert
    else:
        print "Item bisher nicht benutzbar"

def eventhandleGegner(spieler,gegner):
    """Laesst den Gegner eine Aktion ausfuehren"""
    schaden = Angriff(gegner,spieler)
    spieler.energie -= schaden
    
def eventhandleSpieler(aktion,spieler,gegner):
    """Laest den Spieler eine Aktion ausfuehren"""
    if aktion == "angriff":
        schaden = Angriff(spieler,gegner)
        gegner.energie -= schaden
    elif aktion == "heilung":
        heil = ItemUse(Items.Heiltrank())
        spieler.energie += heil
        if spieler.energie > spieler.maxenergie:
            spieler.energie = spieler.maxenergie
            
def anzeigen(spieler,gegner):
    """ Zeigt Energie von Gegner und Spieler an, erstmal provisorisch"""
    print "Kampf: \n%s \t Energie: %i" %(spieler.name,spieler.energie)
    print "%s \t Energie: %i" %(gegner.name,gegner.energie)

def Kampf(spieler,gegner):
    """Startet einen Kampf zwischen Spieler und Gegner, bis einer der beiden keine Energie mehr hat
    Usereingaben sind moeglich wie Item oder Angriff"""
    beendet = False
    aktion = "angriff"
    aktionszaehler = 0
    uhr = pygame.time.Clock()
    while True and beendet == False:
        uhr.tick(30)
        for event in pygame.event.get():                    # Eingabehandling
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    aktion = "angriff"
                elif event.key == pygame.K_h:
                    aktion = "heilung"
        anzeigen(spieler,gegner)
        aktionszaehler += 1                                 # Bestimmt wann der Spieler oder der Gegner Aktionen ausführen können
        if aktionszaehler % (150 - spieler.tempo) == 0:
            print "Spieler greift an"
            eventhandleSpieler(aktion,spieler,gegner)
        if aktionszaehler % (150 - gegner.tempo) == 0:
            print "Gegner greift an"
            eventhandleGegner(spieler,gegner)
        if spieler.energie <= 0:
            print "Spieler tot"
            beendet = True
        elif gegner.energie <= 0:
            print "Gegner besiegt"
            beendet = True
    
    