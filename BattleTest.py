import Monster,Players,Items,Battle,pygame

spieler = Players.Player()
gegner = Monster.Goblin()
pygame.init()
spieler.waffe = Items.Axt()
Battle.Kampf(spieler,gegner)