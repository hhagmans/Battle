class Player():
    """ Erstellt den Spieler mit seinen Standardattributen, nur für den Spielstart vorgesehen"""
    def __init__(self):
        self.name = "Spieler 1"
        self.energie = 100
        self.maxenergie = 100
        self.angriff = 5
        self.verteidigung = 5
        self.geschicklichkeit = 5
        self.tempo = 5