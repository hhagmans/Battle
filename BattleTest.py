import Items,Monster,Players,Battle, datetime, time

def anzeigen():
    print "Kampf: \n%s \t Energie: %i" %(spieler.name,spieler.energie)
    print "%s \t Energie: %i" %(gegner.name,gegner.energie)

def eventhandleGegner():
    schaden = Battle.Angriff(gegner,spieler)
    spieler.energie -= schaden
    
def eventhandleSpieler(aktion):
    if aktion == "angriff":
        schaden = Battle.Angriff(spieler,gegner)
        gegner.energie -= schaden
    elif aktion == "heilung":
        heil = Battle.ItemUse(item)
        spieler.energie += heil
        
    
    
spieler = Players.Player()
gegner = Monster.Goblin()
beendet = False
aktion = "angriff"
startzeit = datetime.datetime.now()

while beendet == False:
    anzeigen()
    #eingabe = raw_input("a: Angriff h: Heilung").lower()
    #if eingabe == "a"
     #   aktion = "angriff"
    #elif eingabe == "h":
     #   aktion = "heilung"
    aktZeit = datetime.datetime.now()
    diff = aktZeit - startzeit
    if diff.seconds % spieler.tempo == 0:
        print "Spieler greift an"
        eventhandleSpieler(aktion)
    if diff.seconds % gegner.tempo == 0:
        print "Gegner greift an"
        eventhandleGegner()
    if spieler.energie <= 0:
        print "Spieler tot"
        beendet = True
    elif gegner.energie <= 0:
        print "Gegner besiegt"
        beendet = True
    time.sleep(1)
    
    