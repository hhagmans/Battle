import Items

class Player():
    """ Erstellt den Spieler mit seinen Standardattributen, nur fuer den Spielstart vorgesehen"""
    def __init__(self):
        self.name = "Spieler 1"
        self.energie = 100
        self.maxenergie = 100
        self.angriff = 5
        self.verteidigung = 5
        self.geschicklichkeit = 5
        self.tempo = 5
        self.waffe = Items.Nichts()
        self.ruestung = Items.Nichts()
        self.hose = Items.Nichts()
        self.schuhe = Items.Nichts()
        self.helm = Items.Nichts()